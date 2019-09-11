|seq| and |par|
===============

Clips can be played one after another by putting them into a |seq|
(which means "sequential") element.

To play two or more clips at the same time, you can put them into a |par|
(which means "parallel") element.

|seq| and |par| elements can be arbitrarily nested.

For a simple example, see :download:`scenes/seq-par.asd`:

.. literalinclude:: scenes/seq-par.asd

If there is no |body| element,
the main :doc:`asdf` element implicitly behaves like a |seq| element,
i.e. all elements are played in sequence,
like in the example file :download:`scenes/implicit-seq.asd`:

.. literalinclude:: scenes/implicit-seq.asd
