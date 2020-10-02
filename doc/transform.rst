|transform|
===========

A constant transform can be simply added to a |clip| element,
like the ``pos`` attribute in :download:`scenes/minimal.asd`:

.. literalinclude:: scenes/minimal.asd

Such attributes (``pos``, ``rot`` etc.) can be added to
:doc:`clip-channel` elements,
as well as :doc:`source` and :doc:`reference` elements.

These attributes can be seen as shorthand notation to avoid using
|transform| elements for such simple cases.
Of course, explicit |transform| elements can also be used,
as shown in :download:`scenes/minimal-expanded.asd`:

.. literalinclude:: scenes/minimal-expanded.asd

``apply-to``
------------

The required attribute ``apply-to`` defines the target(s) for the transform.
This can be the ID or a space-separated list of IDs of any
:doc:`source`, :doc:`clip-channel` elements,
as well as other |transform| elements.
The special ID ``"reference"`` can be used to target the reference.

``pos``
-------

TODO

``rot``
-------

TODO

|o|
---

Typically, |transform| elements contain one or more |o| elements.
Let's call them *transform nodes*.

As we have seen above,
a single |o| element is able to describe a constant transform.

If we specify two transform nodes,
we can define a *linear movement* between two points.
This is shown in :download:`scenes/two-pos.asd`:

.. literalinclude:: scenes/two-pos.asd

You can also specify two rotations, which leads to a linear interpolation
between them.  See :download:`scenes/two-rot.asd`:

.. literalinclude:: scenes/two-rot.asd

In fact, two nodes are not a special case.
As soon as there is more than one node,
a spline is constructed that passes through all the nodes.
In the case of two nodes, this leads to a linear path,
but with more than two nodes, curved trajectories can be created,
as for example in :download:`scenes/minimal-spline.asd`:

.. literalinclude:: scenes/minimal-spline.asd


``time``
^^^^^^^^

By default, sources move with a constant speed along trajectories,
but if desired, time values can be assigned to any node.
The speed will be varied such that the source passes those nodes
at the given times.
See :download:`scenes/spline-time.asd`:

.. literalinclude:: scenes/spline-time.asd

If not specified otherwise, time values are interpreted as seconds.
Hours and minutes can be spelled in ``HH:MM:SS.sss`` format
(where hours and fractions of seconds are optional)
or using the ``h`` and ``min`` suffixes.
For an example, see :download:`scenes/spline-time-hh-mm-ss.asd`:

.. literalinclude:: scenes/spline-time-hh-mm-ss.asd

Time values can also be given in percent,
where 100% is the total duration of the |transform|.
See :download:`scenes/spline-time-percent.asd`:

.. literalinclude:: scenes/spline-time-percent.asd


``speed``
^^^^^^^^^

In addition to time values, concrete speed values can also be specified.
However, not all speed values are allowed.
In order to provide smooth movements,
the possible speed values are limited to a certain range.
The speed is given in meters per second.

For an example, see :download:`scenes/spline-speed.asd`:

.. literalinclude:: scenes/spline-speed.asd


``tension``/``continuity``/``bias``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ASDF uses :doc:`euclidean/kochanek-bartels`, which means that
``tension``, ``continuity`` and ``bias`` attributes
(each value ranging from ``-1.0`` to ``1.0`` with a default of ``0.0``)
can be used, see e.g. :download:`scenes/spline-tcb.asd`:

.. literalinclude:: scenes/spline-tcb.asd

Those attributes can also be used with ``rot`` values, leading to
:doc:`rotation/kochanek-bartels`.


Nested |transform|
------------------

TODO


Empty |transform|
-----------------

TODO: groups
