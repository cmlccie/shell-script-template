#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Executable Python shell script template.

Python shell script template to provide basic script structure, incorporating
personal best practices.

Including:

+ Python v2 & v3 compatibility
+ Verbosity printing
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

# Third-party imports

# Local imports


# Script metadata
__license__ = "MIT"
__copyright__ = "Copyright 2016, Chris Lunsford"
__author__ = "Chris Lunsford"
__email__ = "chris@cmlccie.com"
__credits__ = []
__version__ = "v0.2"
__status__ = "Beta"
__dependencies__ = ['future']

# Initialize logging
logger = logging.getLogger(__name__)
try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logger.addHandler(NullHandler())
console_handler = None
log_handler = None


# Global CONSTANTS


# Global Variables
script_args = None
verbosity = 0


# Helper Functions
def vprint(message_level, *args, **kwargs):
    """Verbosity print function.

    Prints *args objects using **kwargs params if the verbosity level is
    greater than message_level.

    message_level zero '0' indicates a 'quiet' mode; no messages will be
    printed to the console; however, the messages will be logged as INFO
    events.

    All vprint lines are logged as INFO events.

    """
    if message_level >= verbosity > 0:
        print(*args, **kwargs)

    # Log INFO event
    sep = kwargs.get('sep', ' ')
    text = sep.join(args)
    logger.info(text)


# Core Functionality - Functions


# Core Functionality - Classes


# Shell Script / CLI Functions
def parse_args():
    """Parse command-line arguments."""
    # Argparse Tutorial - https://docs.python.org/2/howto/argparse.html
    # Argparse Reference - https://docs.python.org/3/library/argparse.html

    # Create parser
    parser = argparse.ArgumentParser(description=__doc__)

    # Optional Arguments
    parser.add_argument("-v", "--verbosity", help="increase verbosity "
                        "(default is -v)", action="count", default=1)
    parser.add_argument("-q", "--quiet", help="quiet mode; "
                        "overrides the -v option", action="store_true")
    parser.add_argument("-l", "--log-file", help="logs logging messages to "
                        "specified log file")
    parser.add_argument("--debug", action="store_true",
                        help="enables debugging and logs messages to the "
                             "specified log file (requires -l)")

    # Positional Arguments

    # Parse the script arguments
    script_args = parser.parse_args()

    # Set defaults and overrides
    if script_args.quiet:
        script_args.verbosity = 0

    return script_args


def setup_console(log_level=logging.WARNING):
    global console_handler
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(
        logging.Formatter('[%(levelname)-8s] %(message)s'))
    root_logger.addHandler(console_handler)


def setup_logfile(file_path, debug=False):
    global log_handler
    log_level = logging.DEBUG if debug else logging.INFO
    log_handler = logging.FileHandler(file_path, mode='a', encoding='utf-8')
    log_handler.setLevel(log_level)
    log_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)-8s %(name)s %(message)s'))
    logger.addHandler(log_handler)


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
        verbosity = script_args.verbosity
        setup_console()
        if script_args.log_file:
            setup_logfile(script_args.log_file, script_args.debug)
        main()
    except Exception as e:
        logger.error(e.message, exc_info=True)
    finally:
        logging.shutdown()
