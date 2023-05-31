ASDF Splines
============

Knowing the details about the splines used in the ASDF
is not necessary to create scenes.
However, it might still be interesting to know
why the shape and behavior of trajectories is the way it is.

A reference implementation of ASDF splines is available at
https://github.com/AudioSceneDescriptionFormat/asdfspline-rust.
This library is implemented in Rust_
and it provides language bindings for C_ and Python_.

.. _Rust: https://www.rust-lang.org/
.. _C: https://www.open-std.org/jtc1/sc22/wg14/
.. _Python: https://www.python.org/

We refer to a
:doc:`general definition of splines and their properties <splines:euclidean/splines>`
and to detailed background information about all the different types of
:doc:`Euclidean splines <splines:euclidean/index>` and
:doc:`rotation splines <splines:rotation/index>`
mentioned here,
including their mathematical derivation and their individual properties.


Position Splines
----------------

The most obvious type of splines in the ASDF are *position splines*.
The idea is that a scene author provides a sequence of positions
in three-dimensional space
and an ASDF library creates a smooth curve that goes through all of them.
The scene author can also provide the times at which the positions
should be reached, as well as -- with certain limitations --
the speed at those positions.

The ASDF uses (cubic)
:doc:`splines:euclidean/kochanek-bartels`,
which provide three parameters per control point:
*tension*, *continuity* and *bias*, which can be abbreviated to *TCB*.
These TCB parameters allow changing the shape of the resulting curve
without changing the original sequence of positions.
The possible values range from -1 to 1, with 0 being the default.
Kochanek--Bartels splines are
a superset of the probably more familiar
:doc:`splines:euclidean/catmull-rom`.
If all TCB values are zero, the two splines are identical.

To be guaranteed to avoid cusps and self-intersections
(assuming default TCB values),
:ref:`splines:/euclidean/catmull-rom-properties.ipynb#Centripetal-Parameterization`
is used.
This, however, means that the parameter values cannot be chosen freely anymore.
Since we want to be able to specify the times
when certain control points are reached
(and to some degree the speed along the trajectory),
we cannot directly interpret the parameter value as elapsed time.
As a first step, we re-parameterize the spline to have constant speed,
which is also known as
:ref:`splines:/euclidean/re-parameterization.ipynb#Arc-Length-Parameterization`.

Having constant speed trajectories is useful,
but only being able to use constant speed is also quite limiting.
Therefore, on top of arc-length parameterization, ASDF splines are also
:ref:`re-parameterized with a monotone spline <splines:/euclidean/re-parameterization.ipynb#Spline-Based-Re-Parameterization>`.
This means that for each position in the spline, we can specify
the time when this position should be reached.
We can even specify the speed at these positions
(as long as the monotonicity of the re-parameterization spline can be maintained).
See the section about :doc:`transform` for details.

It might have been tempting to use :doc:`splines:euclidean/bezier`
due to their widespread use in 2D drawing software.
However, finding appropriate *drag points* in three-dimensional space
is very hard compared to simply defining a sequence of 3D positions.
Similarly, it would be quite cumbersome to explicitly define
three-dimensional tangent vectors for use with :doc:`splines:euclidean/hermite`.


Rotation Splines
----------------

When a scene author provides a sequence of orientations
for sound sources or groups of sound sources,
the values between the given orientations will be smoothly interpolated.

The same kind of splines are used as for positions,
just modified to work with rotations.
Centripetal :doc:`splines:rotation/kochanek-bartels` are used,
which are a superset of :doc:`Catmull--Rom-Like Rotation Splines <splines:rotation/catmull-rom-non-uniform>`.
If specified, the same TCB values apply to both position and rotation splines.
The rotation splines are arc-length parameterized by default,
which means that they have a constant angular speed.
Time instances can be specified for any of the given rotations,
which in turn control the changing angular speeds along the spline.
The angular speed cannot be specified explicitly, though.
This would be technically possible,
but it is currently not implemented
because specifying an angular speed (for example in degrees per second)
seems unintuitive.
However, this might be added in a future ASDF version.


Volume Splines
--------------

The volume of the :doc:`reference`, of :doc:`source` elements
and of groups of sources can be changed over time.
Since volume can be applied just as translation and rotation,
it is part of the :doc:`transform` attributes,
which can be applied to anything that has an ``id`` attribute.

Volume values should change smoothly,
so they are controlled with splines as well.
An important property of those splines is
that they must not produce interpolated values that overshoot
the given local maximum values,
nor should they produce negative values.
This can be ensured by using
:doc:`splines:euclidean/piecewise-monotone`.
