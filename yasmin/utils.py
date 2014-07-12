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


def normalise_dir_name(dir_name):
    prefix, postfix = '', ''
    if dir_name[0] == '~':
        prefix = os.path.expanduser('~')
        if len(dir_name) == 1:
            dir_name = prefix
        else:
            dir_name = prefix + dir_name[1:]
    if dir_name[len(dir_name) - 1] == '/':
        postfix = '/'
    return dir_name + postfix
