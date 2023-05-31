Special Shapes
==============

There are no pre-defined special shapes in the ASDF.
All trajectories use the same underlying type of spline
-- see :doc:`splines`.


Square
------

Trajectories in the ASDF are smooth curves by default,
and a little extra effort is required to create movements with sharp corners.
There are two simple settings to get straight line segments:
``tension="1"`` or ``continuity="-1"``.
Both options are shown in :scene-link:`square.asd`:

.. literalinclude:: scenes/square.asd


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


Sinusoidal Oscillation
----------------------

Sine waves are not directly supported by the ASDF,
but they can be approximated to some degree.
By setting ``speed="0"`` at the desired maxima and minima,
something similar to sine and cosine oscillations can be created.
This is illustrated in :scene-link:`sine-wave.asd`:

.. literalinclude:: scenes/sine-wave.asd


Lissajous Figures
-----------------

Once we have sinusoidal oscillations (or at least something similar),
we can make `Lissajous figures`__, as shown in :scene-link:`lissajous.asd`:

.. literalinclude:: scenes/lissajous.asd

__ https://en.wikipedia.org/wiki/Lissajous_curve
