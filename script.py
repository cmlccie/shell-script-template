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
import logging
import os
import sys

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


# Setup logging
def get_logger_name():
    if __name__ == "__main__" and sys.argv:
        return os.path.basename(sys.argv[0])
    else:
        return __name__
logging.basicConfig(level=logging.WARNING,
                    format='%(name)s %(levelname)-8s %(message)s')
logger = logging.getLogger(get_logger_name())


# Global CONSTANTS

# Global Variables
script_args = None


# Functions
def parse_args():
    """Parse command-line arguments."""
    # Argparse Tutorial - https://docs.python.org/2/howto/argparse.html
    # Argparse Reference - https://docs.python.org/3/library/argparse.html

    # Create parser
    parser = argparse.ArgumentParser(description=__doc__)

    # Optional Arguments
    parser.add_argument("-v", "--verbosity", help="increase verbosity",
                        action="count", default=0)
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("-lf", "--log-file")

    # Parse the script arguments and return the result
    return parser.parse_args()


def setup_environment():
    if script_args.debug:
        logger.setLevel(logging.DEBUG)
    if script_args.log_file:
        setup_logfile(script_args.log_file)


def setup_logfile(file_path):
    level = logging.DEBUG if script_args.debug else logging.INFO
    formater = logging.Formatter('%(asctime)s %(name)s %(levelname)-8s '
                                 '%(message)s')
    file_handler = logging.FileHandler(file_path, mode='a', encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)


def vprint(message_level, *args, **kwargs):
    """Verbosity print function.

    Prints *args objects using **kwargs params if the verbosity level is
    greater than message_level.  All printed lines are also logged as INFO
    events.

    """
    if  script_args.verbosity >= message_level:
        print(*args, **kwargs)

        # Log all printed lines as INFO events
        sep = kwargs.get('sep', ' ')
        text = sep.join(args)
        logger.info(text)


# Classes


# Main Script
def main():
    vprint(0, "Verbosity Level 0")
    vprint(1, "Verbosity Level 1")
    vprint(2, "Verbosity Level 2")
    logger.debug("Debug Event")
    logger.info("Info Event")
    logger.warning("Warning Event")
    logger.error("Error Event")
    logger.critical("Critical Event")


if __name__ == "__main__":
    try:
        script_args = parse_args()
        setup_environment()
        main()
    except Exception as e:
        logger.critical(e.message, exc_info=True)
