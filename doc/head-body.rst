``<head>`` and ``<body>``
=========================

Both ``<head>`` and ``<body>`` are optional.

If there is a ``<head>`` element,
it must be the first sub-element of ``<asdf>``.

The ``<head>`` element can contain :doc:`source` sub-elements.

.. todo:: ``<meta>`` elements in ``<head>``

The ``<body>`` element can directly contain :doc:`seq-par` elements,
as well as :doc:`\<clip\> <clip-channel>` and :doc:`transform` elements.

If the ``<body>`` element contains multiple sub-elements,
it acts like an implicit :doc:`\<seq\> <seq-par>` element.
