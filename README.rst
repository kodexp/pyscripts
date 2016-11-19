Python Scrpts
==================================

|Build Status| |Coverage Status| |Documentation Status|

Overview
========

Tests CI/CD Unittesting

Documentation
=============

See the `user guide <http://pyscripts.readthedocs.org/en/develop/>`__ for
installation & usage API documentation.

Requirements
============

System
~~~~~~

-  Software
-  Python 2.7+ or Python 3.5+

Developer setup
===============

1. Clone:

   -  ``git clone git_url``

2. Install the native libraries 

3. Install Python dependencies:

   ``python setup.py develop``

4. Run unit tests + PyLint

   ``./check-code.sh``

   (this script approximates what is run by Travis. You can
   alternatively run ``py.test`` yourself)

5. **(or)** Run all tests, including integration tests.

``./check-code.sh integration_tests``



.. |Build Status| image:: https://travis-ci.org/feizhang2/pyscripts.svg?branch=develop
   :target: https://travis-ci.org/feizhang2/pyscripts
.. |Coverage Status| image:: https://coveralls.io/repos/feizhang2/pyscripts/badge.svg?branch=develop&service=github
   :target: https://coveralls.io/github/feizhang2/pyscripts?branch=develop
.. |Documentation Status| image:: https://readthedocs.org/projects/pyscripts/badge/?version=develop
   :target: http://pyscripts.readthedocs.org/en/develop/
