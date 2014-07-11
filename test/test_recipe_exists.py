
import os
import shutil

from unittest import TestCase

from yasmin.utils import get_installed_recipes, check_recipe_sanity
from yasmin.utils import get_recipe_dir
from yasmin.logger import ErrorType


def generate_dummy_recipe():
    recipe_list = get_installed_recipes()
    return recipe_list[0] + "-dummy"


def cleanup_dummies():
    shutil.rmtree(get_recipe_dir() + "/" + dummy)


dummy = generate_dummy_recipe()
dummy_base_filename = get_recipe_dir() + "/" + dummy + "/" + dummy


class TestRecipeExists(TestCase):
    def test_detect_uninstalled_recipe(self):
        self.assertEqual(check_recipe_sanity(dummy),
                         ErrorType.RECIPE_NOT_INSTALLED)

    def test_detect_broken_recipe(self):
        os.makedirs(get_recipe_dir() + "/" + dummy)
        open(dummy_base_filename + ".html", 'a').close()
        self.assertEqual(check_recipe_sanity(dummy),
                         ErrorType.RECIPE_BROKEN)

    def test_detect_correct_recipe(self):
        open(dummy_base_filename + ".css", 'a').close()
        self.assertTrue(check_recipe_sanity(dummy))
        cleanup_dummies()

