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
For further details, see :doc:`clip-channel`.

The examples above use a few shorthand notations to make frequently used
scenarios a bit easier to type.
Expanding all the shortcuts used in the first example above would lead to
the full ASDF syntax shown in :download:`scenes/minimal-expanded.asd`:

.. literalinclude:: scenes/minimal-expanded.asd

Please note a few changes to the "minimal" version above:

* An `XML declaration <https://www.w3.org/TR/xml/#sec-prolog-dtd>`__
  has been added, which is optional in XML 1.0 (but not in XML 1.1)

* The :doc:`head-body` elements are optional.
  If there is no ``<body>`` element, all sub-elements of ``<asdf>``
  (except an optional ``<head>`` element)
  are treated as if they were contained in a ``<body>`` element.
  The ``<asdf>`` element (including version number) is always required.

* In the ``<head>`` section there is a separate :doc:`source` element,
  see also :doc:`source-vs-clip-vs-channel`.

* Even though this is not necessary for a mono ``<clip>``,
  a ``<channel>`` element has been provided explicitly.
  It has been associated with the ``<source>`` that was defined in ``<head>``.
  See also :doc:`source-vs-clip-vs-channel`.

* Even though simple transformations (like specifying a fixed position)
  can be added to :doc:`clip-channel` elements,
  a separate :doc:`transform` element has been used here.
  The target of the ``<transform>`` is the ``<clip>`` element
  (it could also be the ``<channel>`` or the ``<source>`` element,
  which in this simple example wouldn't make any difference).

* Because the ``<clip>`` and the ``<transform>`` happen at the same time,
  they are wrapped in a ``<par>`` element, see :doc:`seq-par`.
  Without this ``<par>`` element, the ``<transform>`` would only be active
  *after* the ``<clip>`` is finished (because the ``<body>`` element implicitly
  behaves like a ``<seq>`` element).
