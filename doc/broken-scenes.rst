.. highlight:: none

Broken ASDF Scenes
==================

Scene files can be broken in many ways, this page tries to list most of them.

:download:`scenes/broken/not-well-formed.asd`:

.. literalinclude:: scenes/broken/not-well-formed.asd

There are many ways an XML file can fail to be
`well-formed <https://www.w3.org/TR/REC-xml/#sec-well-formed>`__,
this is just one example::

   scenes/broken/not-well-formed.asd:1: parser error : Start tag expected, '<' not found
   asdf version="0.4">
   ^


:download:`scenes/broken/no-asdf.asd`:

.. literalinclude:: scenes/broken/no-asdf.asd

::

   Error loading "scenes/broken/no-asdf.asd": The root element must be <asdf>
   ---
   <asd version="0.4">
    ^


:download:`scenes/broken/no-version.asd`:

.. literalinclude:: scenes/broken/no-version.asd

::

   Error loading "scenes/broken/no-version.asd": "version" attribute is required in <asdf> element
   ---
   <asdf>
    ^


:download:`scenes/broken/wrong-version.asd`:

.. literalinclude:: scenes/broken/wrong-version.asd

::

   Error loading "scenes/broken/wrong-version.asd": Only ASDF version 0.4 is supported
   ---
   <asdf version="0.1">
   </asdf>
   ^
