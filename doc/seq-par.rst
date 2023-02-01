|seq| and |par|
===============

Both audio clips (see :doc:`clip-channel`)
and :doc:`transform` elements
are objects that have a certain duration.
They can be placed in the timeline
one after another by putting them into a |seq|
(which means "sequential") element.
To delay an object or to create a pause between two objects,
a :doc:`wait` element can be inserted into the sequence.

To reproduce two or more clips and/or |transform| elements at the same time,
you can put them into a |par| (which means "parallel") element.

|seq| and |par| elements can be arbitrarily nested.

For a simple example, see :scene-link:`seq-par.asd`:

.. literalinclude:: scenes/seq-par.asd

If there is no |body| element,
the main :doc:`asdf` element implicitly behaves like a |seq| element,
i.e. all elements are played in sequence,
like in the example file :scene-link:`implicit-seq.asd`:

.. literalinclude:: scenes/implicit-seq.asd

|seq| and |par| elements can be repeated, see :doc:`repeat`.
