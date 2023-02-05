Special Shapes
==============

There are no pre-defined special shapes in the ASDF.
All trajectories are using the same underlying type of spline
(see :doc:`splines`).


Circle
------

Non-rational cubic polynomial curves
-- which is the type of curve the ASDF uses for position trajectories --
cannot exactly describe circles.
But this is no problem, because circles can be approximated very closely.
This can be done by providing the corner points of a square
and using a ``tension`` value of about ``-0.66``.
However, there is actually a way to create exact circles:
by applying a rotation spline to a translated object.
The example scene :scene-link:`circle.asd` shows both approaches:

.. literalinclude:: scenes/circle.asd

In this example, the center of rotation is the origin.
If the center of rotation is supposed to be somewhere else,
it can be moved by applying a new |transform| element
with the desired ``pos`` attribute
to the |transform| that does the rotation.


Helix
-----

A helical movement can be created by combining a (repeated)
circular movement (using one of the methods shown above)
with a linear movement perpendicular to the plane of the circle.
This is shown in :scene-link:`helix.asd`:

.. literalinclude:: scenes/helix.asd

In this example,
the |clip| is offset to the left
and a rotation spline rotates this offset multiple times around the *roll* axis.
This circular motion is then translated along the default view direction.
In this case,
it doesn't matter if ``forward-motion`` is applied to ``circular-motion``
or directly to ``ukulele``.
