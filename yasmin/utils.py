import os

from yasmin.logger import report_error, ErrorType


def get_root_dir():
    return os.path.expanduser('~') + "/yasmin"


def get_recipe_dir():
    return get_root_dir() + "/recipes"


def get_installed_recipes():
    return os.listdir(get_recipe_dir() + "/")


def check_recipe_sanity(recipe):
    package_dir = get_recipe_dir()
    if recipe not in os.listdir(package_dir):
        return report_error(ErrorType.RECIPE_NOT_INSTALLED, recipe)
    recipe_dir = package_dir + "/" + recipe + "/"
    if (recipe + ".html") not in os.listdir(recipe_dir) \
            or (recipe + ".css") not in os.listdir(recipe_dir):
        return report_error(ErrorType.RECIPE_BROKEN, recipe)
    else:
        return True
