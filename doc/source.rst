|source|
========

|source| elements are defined within the |head| element
and all sources exist for the entire duration of the scene.


File Inputs
-----------

:doc:`clip-channel` elements can provide audio signals for |source| elements
using the ``source`` attribute.
If no ``source`` attribute is given, an unnamed |source| is implicitly created.

A |source| can be fed by multiple |clip| elements over time,
but only if they don't overlap.
If the ``port`` attribute (see below) is given,
no |clip| elements can be assigned.

An implementation may re-use the same unnamed |source|
for multiple non-overlapping |clip| elements, but this is not required.


Live Inputs
-----------

The ``port`` attribute can be used to provide live input signals,
for example from microphones, external sound hardware or
any software capable of producing audio signals
(and connecting them with the software loading the ASDF scene).

The content of the ``port`` attribute isn't strictly specified and
it is up to the reproduction software to interpret it.

For example, the SSR_ provides an ``--input-prefix`` option
to which the content of the ``port`` attribute is appended.
By default, the prefix is ``system:capture_`` and appending numbers starting
with ``1`` will select the corresponding hardware input channels.

.. _SSR: http://spatialaudio.net/ssr/

The scene :scene-link:`live-sources.asd` shows an example of
using the first 4 hardware inputs as sources:

.. literalinclude:: scenes/live-sources.asd

Live sources and sources driven by audio files can be mixed in one scene and
:doc:`transform` elements can apply to either.
See e.g.  :scene-link:`live-sources-and-file-sources.asd`:

.. literalinclude:: scenes/live-sources-and-file-sources.asd


Transform Attributes
--------------------

Any |source| element with an ``id`` attribute can be the target of a
:doc:`transform` (using the ``apply-to`` attribute).
Like :doc:`clip-channel`,
|source| can also use transform attributes
like ``pos``, ``rot`` etc. as a shortcut,
see :scene-link:`source-transform.asd`:

.. literalinclude:: scenes/source-transform.asd
