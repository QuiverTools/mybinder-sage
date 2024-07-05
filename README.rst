A Binder repository for using QuiverTools
=========================================

This repository is a Binder repository based on `SageMath <https://sagemath.org>`_
which comes with `QuiverTools <https://quiver.tools>`_ installed,
together with some easy examples.

To run this, just click on the badge:

.. image:: https://mybinder.org/badge_logo.svg
 :target: https://mybinder.org/v2/gh/QuiverTools/mybinder-sage/master

Authors
-------

Pieter Belmans

Based on https://github.com/sagemath/sage-binder-env by
Nicolas M. Thiéry, E. Madison Bray, and Kwankyu Lee

Instructions to ourselves
=========================

With `jupytext` one can convert between `.py` and `.ipynb`.
In particular, the following

.. code-block::
   jupytext --to ipynb src/basic.py
   mv src/basic.ipynb notebooks

converts the very rudimentary proof of concept to a notebook.

I have left the result of `jupytext --to py start.ipynb`, which is the
example provided in the original repository, in the `/src` directory,
so that we know which syntax to use.
