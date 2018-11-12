Position and Orientation
========================

The ASDF uses a right-handed cartesian coordinate system
to specify positions in 3D space.
The x-, y- and z-axis can be thought of  as pointing towards
*east*, *north* and *up*, respectively,
which is sometimes called an *ENU* system
(see https://en.wikipedia.org/wiki/Axes_conventions).
However, contrary to typical ENU systems,
the default orientation in the ASDF is towards *north*,
i.e. towards the positive y-axis!

Imagine a treasure map lying on a table in front of you.
The north direction typically points towards the top of the map
and the east direction points to the right.
On the other hand, if you had a piece of paper with a mathematical graph on it,
the y-axis would point towards the top of the page
and the x-axis would point to the right.
Therefore it makes sense that the x-axis points towards east
and the y-axis points northwards, right?

Now imagine that you are sitting at the table
with your treasure map in front of you.
Your will look straight ahead by default,
and this happens to be northwards on the map.
Therefore, the default orientation in ASDF is towards north,
which corresponds to the positive y-axis.

To complete the triple of axes, the z-axis points up to the ceiling
(or towards the zenith, if your table is in open air).
Positive z-values are above the table, negative z-values are below the table.
The resulting coordinate system is right-handed, which is convenient.
