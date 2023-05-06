|asdf|
======

An ASDF file must contain a single top-level |asdf| element
with a required ``version`` attribute.
Currently, only ``version="0.4"`` is supported.

The |asdf| element can optionally contain :doc:`head-body` sub-elements.

If there is no |body| element, all sub-elements of |asdf|
(except an optional |head| element)
are treated as if they were contained in a |body| element,
which in turn behaves like an implicit :doc:`\<seq\> <seq-par>`,
see :doc:`head-body`.
For example, the clips in :scene-link:`implicit-seq.asd`
are played in sequence:

.. literalinclude:: scenes/implicit-seq.asd
