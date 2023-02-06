|clip| and |channel|
====================

To load an audio file,
a |clip| element can be inserted at the spot
in the timeline where it should be played back.
Each |channel| of a multi-channel file
can have its own static transform attributes
(``pos``, ``rot``, etc.), as shown in the example scene
:scene-link:`minimal-multichannel.asd`:

.. literalinclude:: scenes/minimal-multichannel.asd

If the audio file only has a single channel,
an explicit |channel| element is not necessary.
If desired, transform attributes can be applied to the |clip| element itself,
see :scene-link:`minimal.asd`:

.. literalinclude:: scenes/minimal.asd

Volume control is part of the :doc:`transform` mechanism.
A constant volume can be specified with the ``vol`` attribute
of |clip| and/or |channel|, a dynamic volume envelope can be applied
with a |transform| element that's running in parallel to the |clip|
(see :doc:`seq-par`).

As :scene-link:`selecting-channels.asd` shows,
not all channels of a |clip| have to be used:

.. literalinclude:: scenes/selecting-channels.asd

Audio clips are always played to their full length.
Audio files should be trimmed beforehand to the desired length.


``repeat``
----------

|clip| elements can be repeated, see :doc:`repeat`.


``id``
------

Both |clip| and |channel| elements can be the target of a :doc:`transform`,
as long as they have an ``id`` attribute.
|transform| and |clip| can have differing begin and end times.
A single |transform| can apply to multiple |clip| and/or |channel| elements.
A |clip| can be transformed by multiple |transform| elements over time.
The |transform| elements can overlap,
but only one of them can contain a rotation in this case.


``source``
----------

If no ``source`` attribute is given,
a |source| is created implicitly for each channel.
The order of implicit sources is unspecified.
An implementation may re-use an implicit source for multiple clips
(as long as the clips don't overlap in time), but this is not required.

Individual audio channels can also be explicitly assigned
to existing :doc:`source` elements,
as demonstrated in :scene-link:`source-transform.asd`:

.. literalinclude:: scenes/source-transform.asd

This illustrates that different |channel| elements
can be assigned to the same |source|.
However, this only works if the channels don't overlap in time.
