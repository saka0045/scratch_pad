import unittest

from cpi_duty_rotator import *


class TestParseRotatorIndexFile(unittest.TestCase):
    def setUp(self):
        self.rotator_file = open("/Users/m006703/scratch_pad/test_duty_rotator_index.txt", "r")

        self.rotator_index_dict = {}

        self.rotator_index_dict_out = {'is_rotator_index': 4, 'spa_rotator_index': 0}

    def test_parse_roator_index_file_happy(self):
        parse_rotator_index_file(self.rotator_file, self.rotator_index_dict)
        self.assertEqual(self.rotator_index_dict_out, self.rotator_index_dict,
                         "failed parse_rotator_index_file")

    def doCleanups(self):
        self.rotator_file.close()
