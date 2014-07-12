
from unittest import TestCase

from yasmin.logger import ErrorType
from yasmin.utils import normalise_dir_name
from yasmin import yasmin


class TestParseArguments(TestCase):
    def test_valid_number_but_invalid_argument(self):
        args1 = ["-g", "foo", "-d", "boo", "moe"]
        test1 = yasmin.parse_arguments(args1)
        self.assertEqual(test1, ErrorType.INVALID_ARGUMENTS)

    def test_invalid_number_of_arguments(self):
        args1 = ["-g"]
        test1 = yasmin.parse_arguments(args1)
        self.assertEqual(test1, ErrorType.NOT_ENOUGH_ARGUMENTS)

    def test_valid_arguments(self):
        args1 = ["-lang", "cpp", "-ds", "array", "~"]
        test1 = yasmin.parse_arguments(args1)
        norm_output_dir = normalise_dir_name(args1[4])
        self.assertDictEqual(test1, {
            "data_structure": "array",
            "language": "cpp",
            "output_dir": norm_output_dir
        })
        args2 = ["-ds", "array", "-lang", "cpp","~"]
        test2 = yasmin.parse_arguments(args2)
        self.assertDictEqual(test1, test2)
