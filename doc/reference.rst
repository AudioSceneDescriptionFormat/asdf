|reference|
===========

The so-called *reference point* is a generalization of a *listener point*.
In a headphone-based reproduction system it corresponds
to the position (and orientation) of the listener's head in the virtual scene.
In a loudspeaker-based system there might be multiple listeners,
but the loudspeaker setup should still have a single *reference point*,
which is typically somewhere in the center of the setup.

There is only one |reference| element,
and it implicitly has the reserved ID ``"reference"``,
which can be used as the target of a :doc:`transform`.

The |reference| can be specified explicitly within the |head| element
and it can optionally have static transform attributes like ``pos`` and ``rot``,
as in the example scene :scene-link:`reference-transform.asd`:

.. literalinclude:: scenes/reference-transform.asd

If no |reference| element is given,
the reference point can still be transformed using ``apply-to="reference"``,
as in :scene-link:`implicit-reference.asd`:

.. literalinclude:: scenes/implicit-reference.asd
