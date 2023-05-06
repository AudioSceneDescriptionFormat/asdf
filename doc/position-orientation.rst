Position and Orientation
========================

The ASDF uses a right-handed cartesian coordinate system
to specify positions in three-dimensional space.
The x-, y- and z-axis can be thought of  as pointing towards
*east*, *north* and *up*, respectively,
which is sometimes called an `ENU system`__.
However, contrary to typical ENU systems,
the default orientation in the ASDF is towards *north*,
i.e. along the positive y-axis!

__ https://en.wikipedia.org/wiki/Axes_conventions

To understand the motivation for this choice of default orientation,
imagine a treasure map lying on a table in front of you.
The north direction typically points towards the top of the map
and the east direction points to the right.
On the other hand, if you had a piece of paper with a mathematical graph on it,
the y-axis would point towards the top of the page
and the x-axis would point to the right.
Therefore it makes sense that the x-axis points towards east
and the y-axis points northwards, right?
Now imagine that you are sitting at the table
with your treasure map in front of you.
You will look straight ahead by default,
and this happens to be northwards on the map.
Therefore, the default orientation in the ASDF is towards north,
which corresponds to the positive y-axis.
To complete the triple of axes, the z-axis points up to the ceiling
(or towards the zenith, if your table is in open air).
Positive z-values are above the table, negative z-values are below the table.
The resulting coordinate system is right-handed, which is convenient.

The coordinate values for positions are given in meters.
The third coordinate is optional and defaults to zero.

As mentioned above,
the default orientation (sometimes called *view* direction)
is along the positive y-axis.
To fully specify all three degrees of freedom,
the default *up* direction is set to the positive z-axis
(which should be an unsurprising choice).
For specifying arbitrary rotations relative to this default orientation,
up to three `Tait--Bryan angles`__ can be specified.
The first angle (*azimuth*) rotates around the z-axis,
the second angle (*elevation*) around the (previously rotated) x-axis
and the third angle (*roll*) around the (previously rotated) y-axis.

__ https://en.wikipedia.org/wiki/Euler_angles#Tait–Bryan_angles

All angles are given in degrees.
The *elevation* and *roll* angles are optional, with a default of zero.
The sign of the rotation angles follows the `right hand rule`__.
Rotations are specified in degrees because that is familiar to most people.
However, for any further calculations in an ASDF library,
the angles should be immediately converted
to quaternions or rotation matrices, see :doc:`implementation`.

__ https://en.wikipedia.org/wiki/Right-hand_rule#Rotations

Multiple translations/rotations can be nested,
which means that all coordinates are local with respect to the parent transform.
For more details, see :ref:`nested-transform`.
