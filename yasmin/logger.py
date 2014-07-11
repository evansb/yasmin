
from enum import Enum

import sys


class ErrorType(Enum):
    FATAL,\
        OUTPUT_DIR_EQUAL_VENDOR,\
        NOT_ENOUGH_ARGUMENTS,\
        INVALID_ARGUMENTS,\
        PACKAGE_DIRECTORY_MISSING,\
        RECIPE_NOT_INSTALLED, \
        RECIPE_BROKEN = list(range(7))


def exit_unless_testing(is_test_mode=False):
    if not is_test_mode:
        exit(0)


def handle_fatal(error):
    sys.stdout.write("fatal error. exiting yasmin\n")
    exit_unless_testing(__debug__)


def handle_output_dir_equal_vendor(error):
    sys.stdout.write("error: output dir must not equal vendor dir\n")


def handle_not_enough_arguments(error):
    sys.stdout.write("error: not enough arguments supplied\n")


def handle_invalid_arguments(error):
    sys.stdout.write("error: invalid arguments")


# TODO: Finish this
def handle_recipe_broken(error):
    pass


# TODO: Finish this
def handle_recipe_not_installed(error):
    pass


def report_error(error_type=ErrorType.FATAL, error=None):
    if not __debug__:
        func_name = "handle_" + error_type.name.lower()
        eval(func_name + "(error)", globals(), locals())
    return error_type
