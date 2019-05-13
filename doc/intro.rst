Introduction
============

Let's start simple, with the file :download:`scenes/minimal.asd`:

.. literalinclude:: scenes/minimal.asd

This plays the contents of the (mono) audio file
:download:`scenes/audio/ukewave.ogg`,
coming from a spatial position of 2 metres in front and 1 metre to the right.
For more details on the used coordinate system, see :doc:`position-orientation`.

If you want to play a file with more than one channel,
you have to provide positions for each of the channels,
like shown in :download:`scenes/minimal-multichannel.asd`:

.. literalinclude:: scenes/minimal-multichannel.asd

This plays the contents of the (two-channel) audio file
:download:`scenes/audio/marimba.ogg`,
each channel coming from its specified position.

.. todo:: How to select a subset of channels
