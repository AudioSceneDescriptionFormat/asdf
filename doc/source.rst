|source|
========

TODO

See :doc:`source-vs-clip-vs-channel`.

Transform Attributes
--------------------

Like :doc:`clip-channel` elements, |source| can also have transform attributes
like ``pos``, ``rot`` etc.

:scene-link:`source-transform.asd`:

.. literalinclude:: scenes/source-transform.asd


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
