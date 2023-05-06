Introduction
============

Let's start simple, with the file :scene-link:`minimal.asd`:

.. literalinclude:: scenes/minimal.asd

This plays the contents of the (mono) audio file
:scene-link:`audio/ukewave.ogg`,
coming from a spatial position of 2 meters in front and 1 meter to the right.
For more details on the used coordinate system, see :doc:`position-orientation`.

If you want to play a file with more than one channel,
you can provide positions for each of the channels,
like shown in :scene-link:`minimal-multichannel.asd`:

.. literalinclude:: scenes/minimal-multichannel.asd

This plays the contents of the (two-channel) audio file
:scene-link:`audio/marimba.ogg`,
each channel coming from its specified position.
For further details, see :doc:`clip-channel`.

The examples above use a few shorthand notations to make frequently used
scenarios a bit easier to type.
Expanding most of the shortcuts used in the first example above would lead to
the more complicated ASDF syntax shown in :scene-link:`minimal-expanded.asd`:

.. literalinclude:: scenes/minimal-expanded.asd

Please note a few changes to the "minimal" version above:

* An `XML declaration <https://www.w3.org/TR/xml/#sec-prolog-dtd>`__
  has been added, which is optional in XML 1.0 (but not in XML 1.1).

* The :doc:`head-body` elements are optional.
  The :doc:`asdf` element (including version number) is always required.

* In the |head| section there is a separate :doc:`source` element.

* The |body| element implicitly behaves like a |seq| element,
  see :doc:`seq-par`.

* Even though this is not necessary for a mono |clip|,
  a |channel| element has been provided explicitly.
  It has been associated with the :doc:`source` that was defined in |head|.

* The z-component in ``pos`` is optional, see :doc:`transform`.

This still uses the shorthand of specifying the position directly in the
|channel| element.
As shown in :scene-link:`minimal-expanded-with-explicit-transform.asd`,
it can be expanded even further:

.. literalinclude:: scenes/minimal-expanded-with-explicit-transform.asd

* Because the |clip| and the |transform| happen at the same time,
  they are wrapped in a |par| element, see :doc:`seq-par`.
  Without this |par| element, the |transform| would only be active
  *after* the |clip| is finished (because the |body| element implicitly
  behaves like a |seq| element).

* If the clip has only one channel, it doesn't matter whether the |transform|
  is applied to the |clip| or to the |channel|.
  In this simple case it could be even directly applied to the |source|.

* The :doc:`transform` element could be even further expanded
  to contain the ``pos`` information in a single |o| sub-element.
