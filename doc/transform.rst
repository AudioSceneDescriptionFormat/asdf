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

|o|
---

Typically, |transform| elements contain one or more |o| elements.
Let's call them *transform nodes*.

As we have seen above,
a single |o| element is able to describe a constant transform.

If we specify two transform nodes,
we can define a *linear movement* between two points.
This is shown in :download:`scenes/minimal-movement.asd`:

.. literalinclude:: scenes/minimal-movement.asd

In fact, two nodes are not a special case.
As soon as there is more than one node,
a spline is constructed that passes through all the nodes.
In the case of two nodes, this leads to a linear path,
but with more than two nodes, curved trajectories can be created,
as for example in :download:`scenes/minimal-spline.asd`:

.. literalinclude:: scenes/minimal-spline.asd

By default, sources move with a constant speed along trajectories,
but if desired, time values can be assigned to any node.
The speed will be varied such that the source passes those nodes
at the given times.

:download:`scenes/spline-time.asd`:

.. literalinclude:: scenes/spline-time.asd

In addition to time values, concrete speed values can also be specified.
However, not all speed values are allowed.
In order to provide smooth movements,
the possible speed values are limited to a certain range.
The speed is given in meters per second.

For an example, see :download:`scenes/spline-speed.asd`:

.. literalinclude:: scenes/spline-speed.asd

Empty |transform|
-----------------

TODO: groups
