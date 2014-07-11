
import argparse
import os
import pystache

from yasmin.logger import report_error, ErrorType
from yasmin.utils import get_root_dir


MINIMUM_ARG_LENGTH = 5


def parse_arguments(args):
    if len(args) < MINIMUM_ARG_LENGTH:
        return report_error(ErrorType.NOT_ENOUGH_ARGUMENTS)
    parser = argparse.ArgumentParser(description="Yasmin")
    parser.add_argument("output_dir", metavar="OUTPUT_DIR",
                        action="store", help="the output directory")
    parser.add_argument("-lang", metavar="LANGUAGE",
                        action="store", dest="language",
                        help="programming language used")
    parser.add_argument("-ds", metavar="DATA_STRUCTURE",
                        action="store", dest="data_structure",
                        help="data structure used")
    return_value = None
    try:
        result = parser.parse_args(args)
        return_value = {
            "output_dir": result.output_dir,
            "language": result.language,
            "data_structure": result.data_structure
        }
    except argparse.ArgumentError as exc:
        report_error(ErrorType.INVALID_ARGUMENTS, exc)
    finally:
        return return_value or ErrorType.INVALID_ARGUMENTS


def copy_and_render_template_to(argdata):
    root_dir = get_root_dir()
    vendor_dir = root_dir + "static/vendor"
    ds = argdata["data_structure"]
    context = {
        "vendor_dir": vendor_dir,
        "data_structure": ds,
        "data_structure_dir": root_dir + "/packages/" + ds
    }
    if os.path.samefile(vendor_dir, argdata["output_dir"]):
        return report_error(ErrorType.OUTPUT_DIR_EQUAL_VENDOR)
    else:
        with open(vendor_dir + "yasmin.html", "r") as template:
            content = pystache.render(template, context)
        with open(argdata["output_dir"] + "yasmin.html", "w") as output_file:
            output_file.write(content)
