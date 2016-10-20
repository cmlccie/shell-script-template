#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executable Python shell script template.

Python shell script template to provide basic script structure, incorporating
personal best practices.

Including:

+ Python v2 & v3 compatibility
+ Argument parsing
+ Logging

**Note:**  To provide Python v2 and v3 compatibility, the script requires the
``future`` package be installed in the executing environment.  This package
may be installed from PyPI as follows:

.. code-block:: bash

    $ pip install future

"""


# Python v2 & v3 compatibility imports
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import *

# Standard library imports
import argparse
# TODO: Setup logging

# Third-party imports

# Local imports


# Script metadata
__author__ = "Chris Lunsford"
__email__ = "chris@cmlccie.com"
__license__ = "MIT"
__copyright__ = "Copyright 2016, Chris Lunsford"
__maintainer__ = "Chris Lunsford"
__credits__ = []
__version__ = "v0.1"
__status__ = "Beta"


# Global CONSTANTS

# Global Variables
script_args = None


# Functions
def parse_args():
    global script_args
    # Create parser
    parser = argparse.ArgumentParser(description=__doc__)
    # Optional Arguments
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    # Parse the script arguments and set defaults
    script_args = parser.parse_args()


# Classes


# Main Script
def main():
    pass


if __name__ == "__main__":
    parse_args()
    main()
