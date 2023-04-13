|head| and |body|
=================

Both |head| and |body| are optional.

If there is a |head| element,
it must be the first sub-element of :doc:`asdf`.

The |head| element can contain :doc:`source` sub-elements
and an optional :doc:`reference` element.
All elements within |head| exist for the whole duration of the scene.
If they contain transform attributes like ``pos`` or ``rot``,
those values are static.
Additional :doc:`transform` elements can be used in the |body|
to offset those values dynamically.

The |body| element can contain :doc:`seq-par` elements,
as well as :doc:`\<clip\> <clip-channel>` and :doc:`transform` elements.
If the |body| element contains multiple sub-elements,
it acts like an implicit :doc:`\<seq\> <seq-par>` element.
