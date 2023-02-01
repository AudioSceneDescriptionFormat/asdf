|transform|
===========

A constant transform can be simply added to a |clip| element,
like the ``pos`` attribute in :scene-link:`minimal.asd`:

.. literalinclude:: scenes/minimal.asd

Such attributes (``pos``, ``rot`` etc.) can be added to
:doc:`clip-channel` elements,
as well as :doc:`source` and :doc:`reference` elements.

These attributes can be seen as shorthand notation to avoid using
|transform| elements for such simple cases.
Of course, explicit |transform| elements can also be used,
as shown in :scene-link:`minimal-expanded-with-explicit-transform.asd`:

.. literalinclude:: scenes/minimal-expanded-with-explicit-transform.asd

``apply-to``
------------

The required attribute ``apply-to`` defines the target(s) for the transform.
This is a space-separated list of IDs of any
:doc:`source`, :doc:`clip-channel` elements,
as well as other |transform| elements.
The special ID ``"reference"`` can be used to target the :doc:`reference`.

A |transform| element can apply to multiple objects.
An object can be the target of multiple transforms,
as long as at most one of them contains a rotation.


``pos``
-------

This is named after *position*, but technically,
the term *translation* would be more appropriate.
The final *position* of a sound source (or the :doc:`reference`)
can be the result of multiple *translations*
(and maybe *rotations* as well, see below)
applied to the default *position* ``(0, 0, 0)``.

The ``pos`` attribute contains a space-separated list
of two or three coordinate values.
If only two values are given, the third one is assumed to be zero.
For coordinate system conventions, see :doc:`position-orientation`.


``rot``
-------

In contrast to ``pos``, this is aptly named after *rotation*.
The final *orientation* of a sound source (or the :doc:`reference`)
can be the result of multiple *rotations*,
applied to the default *orientation* ``(0, 0, 0)``.
For angle conventions, see :doc:`position-orientation`.

The order of applying translations and rotations matters:
within a |transform| element, ``rot`` is applied *after* ``pos``.


``vol``
-------

A (linear) volume change can be specified as a non-negative decimal value.
Using ``vol="0"`` results in silence,
``vol="0.5"`` corresponds to an attenuation of about 6 decibels,
``vol="1"`` doesn't change the volume and
``vol="2"`` corresponds to boost of about 6 decibels.


|o|
---

Typically, |transform| elements contain one or more |o| elements.
Let's call them *transform nodes*.

As we have seen above,
a single |o| element is able to describe a constant transform.

If we specify two transform nodes,
we can define a *linear movement* between two points.
This is shown in :scene-link:`two-pos.asd`:

.. literalinclude:: scenes/two-pos.asd

You can also specify two rotations, which leads to a linear interpolation
between them.  See :scene-link:`two-rot.asd`:

.. literalinclude:: scenes/two-rot.asd

In fact, two nodes are not a special case.
As soon as there is more than one node,
a spline is constructed that passes through all the nodes.
In the case of two nodes, this leads to a linear path,
but with more than two nodes, curved trajectories can be created,
as for example in :scene-link:`minimal-spline.asd`:

.. literalinclude:: scenes/minimal-spline.asd

In addition to ``pos`` and ``rot``, the ``vol`` attribute can also be animated,
see :scene-link:`transform-vol.asd`:

.. literalinclude:: scenes/transform-vol.asd

.. note::

    This should only be used for relatively slow volume changes,
    because the renderer might only apply them on a block-by-block basis.
    If you need fast envelopes, those should be applied by modifying
    the source file in a waveform editor.


.. _transform-time:

``time``
^^^^^^^^

By default, sources move with a constant speed along trajectories,
but if desired, time values can be assigned to any node.
The speed will be varied such that the source passes those nodes
at the given times.
The first node always implicitly has ``time="0"``.
See :scene-link:`spline-time.asd`:

.. literalinclude:: scenes/spline-time.asd

If not specified otherwise, time values are interpreted as seconds.
Hours and minutes can be spelled in ``HH:MM:SS.sss`` format
(where hours and fractions of seconds are optional)
or using the ``h`` and ``min`` suffixes.
For an example, see :scene-link:`spline-time-hh-mm-ss.asd`:

.. literalinclude:: scenes/spline-time-hh-mm-ss.asd

Time values can also be given in percent,
where 100% is the total duration of the |transform|.
See :scene-link:`spline-time-percent.asd`:

.. literalinclude:: scenes/spline-time-percent.asd


``speed``
^^^^^^^^^

In addition to time values, concrete speed values can also be specified.
However, not all speed values are allowed.
In order to provide smooth movements,
the possible speed values are limited to a certain range.
The speed is given in meters per second.

For an example, see :scene-link:`spline-speed.asd`:

.. literalinclude:: scenes/spline-speed.asd


``tension``/``continuity``/``bias``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ASDF uses :doc:`splines:euclidean/kochanek-bartels`, which means that
``tension``, ``continuity`` and ``bias`` attributes
(each value ranging from ``-1.0`` to ``1.0`` with a default of ``0.0``)
can be used, see e.g. :scene-link:`spline-tcb.asd`:

.. literalinclude:: scenes/spline-tcb.asd

Those attributes can also be used with ``rot`` values, leading to
:doc:`splines:rotation/kochanek-bartels`.


Nested |transform|
------------------

Any |transform| that has an ``id`` attribute
can be used as the target of another |transform|.
The transforms can have different begin and end times.
They only have an effect while they are active.

Multiple |transform| elements can target the same object,
but at most one of them can specify a rotation.

An example of nested transforms can be seen in
:scene-link:`nested-transforms.asd`:

.. literalinclude:: scenes/nested-transforms.asd

The |clip| defines a static position,
which is then dynamically translated in the horizontal plane
according to the |transform| named ``horizontal-movement``.
This horizontal movement is then transformed again,
this time with a dynamic rotation around the *roll* axis.
