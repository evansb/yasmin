
import os
import shutil

from unittest import TestCase

from yasmin.yasmin import copy_and_render_template_to, parse_arguments


dummy_dir_path = os.path.expanduser('~') + '/__dummy_dir'
test_arg = ['-lang', 'java', '-ds', 'array', dummy_dir_path]

class TestRenderTemplate(TestCase):
    def setUp(self):
        if os.path.exists(dummy_dir_path):
            shutil.rmtree(dummy_dir_path)
        os.makedirs(dummy_dir_path)
        parsed_arg = parse_arguments(test_arg)
        copy_and_render_template_to(parsed_arg)

    def test_rendered_file_is_created(self):
        self.assertTrue(os.path.exists(dummy_dir_path + '/yasmin.html'))

    def test_rendered_file_is_valid(self):
        with open(dummy_dir_path + '/yasmin.html', 'r') as file:
            blob = file.read()
            self.assertTrue(blob.find(test_arg[3] + '.js'))
            self.assertTrue(blob.find(test_arg[3] + '.css'))

    def tearDown(self):
        shutil.rmtree(dummy_dir_path)

