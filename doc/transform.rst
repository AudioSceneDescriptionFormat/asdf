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
of two or three coordinate values (in meters).
If only two values are given, the third one is assumed to be zero.
For coordinate system conventions, see :doc:`position-orientation`.


``rot``
-------

Unlike ``pos``, this is aptly named after *rotation*.
The final *orientation* of a sound source (or the :doc:`reference`)
can be the result of multiple *rotations*,
applied to the default *orientation* ``(0, 0, 0)``.

The ``rot`` attribute contains a space-separated list of up to three angles
(in degrees) called *azimuth*, *elevation* and *roll*.
Only *azimuth* is required, the others default to zero degree if not specified.
For angle conventions, see :doc:`position-orientation`.

The range of angle values is not limited,
but the represented rotations are cyclically repeating
and the number of turns is irrelevant.
This means that the angles -90 and 270 both specify the same rotation.
When using a sequence of rotations to define a rotation spline
(see the |o| element below),
the smallest possible angular difference between neighboring rotations is used.
For example,
an angle of 270 degrees followed by an angle of 0 degrees
will lead to a rotation of 90 degrees.
An angle of 180 degrees followed by -180 degrees
will lead to no rotation at all.

The order of applying translations and rotations matters:
within a |transform| element, ``pos`` is applied *after* ``rot``.
This means that the target of a |transform| is first rotated
around the (local) origin and then translated to its final position.


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
where 100% is the total duration of (one repetition of) the |transform|.
See :scene-link:`spline-time-percent.asd`:

.. literalinclude:: scenes/spline-time-percent.asd

If the |transform| doesn't have a ``dur`` (see below),
the last node can have an explicit ``time`` value,
but a percentage is not allowed.
If unspecified, ``time="100%"`` is implied, i.e.
the |transform| always ends with the last transform node.

If the ``time`` value of a node is not specified,
it is deduced from the surrounding nodes.


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


Mixed Transform Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^

We have seen that ``pos``, ``rot`` and ``vol`` trajectories can be created.
However, they can also be combined in a single trajectory.

None of the transform attributes are required,
but if one of the attributes is used in any transform node,
it also has to be specified in the first and last node.
In other words,
missing values are interpolated but not extrapolated.

The scene :scene-link:`mixed-transform-attributes.asd`
illustrates this in an example trajectory:

.. literalinclude:: scenes/mixed-transform-attributes.asd


``repeat``
----------

|transform| elements can be repeated, see :doc:`repeat`.


``dur``
-------

If the last transform node has its ``time`` attribute set,
this will determine the duration of the |transform|.

Alternatively, the duration of a |transform|
can be specified with the ``dur`` attribute,
which allows the same syntax as the ``time`` attribute of transform nodes.
If there are repetitions, the duration is that of a single repetition.
A percentage can be given, which is relative to the duration of
(one repetition of) the parent element.

If no duration is given, and the |transform| is part of a |par| container,
the duration is taken from the |par| container
(whose duration might be provided by its first sub-element).
See :doc:`seq-par`.


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


Creating Groups With |transform|
--------------------------------

There is no dedicated "group" element,
but a |transform| with multiple targets in the ``apply-to`` attribute
is essentially defining a group.
All transform attributes are optional,
allowing us to create a group by using a non-transforming |transform|:

.. code::

    <transform id="my-group" apply-to="target1 target2 my-other-target" />

This group can then in turn be the target of further |transform| elements.
