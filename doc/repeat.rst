Repetition
==========

:doc:`\<clip\> <clip-channel>`,
:doc:`transform`,
:doc:`seq-par`
elements can be repeated using the ``repeat`` attribute.
Only full repetitions (i.e. integer values) are supported.

For an example of all elements that support ``repeat``,
see :scene-link:`repeat.asd`:

.. literalinclude:: scenes/repeat.asd

It's not possible to repeat an element forever,
but you might as well just use a huge number of repetitions,
as shown in :scene-link:`repeat-nearly-indefinitely.asd`:

.. literalinclude:: scenes/repeat-nearly-indefinitely.asd
