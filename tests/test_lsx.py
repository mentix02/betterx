"""
unit tests for lsx script
"""
import os
import shutil
import random
import string
import pathlib
import unittest

from betterx import lsx, full_path


def random_string() -> str:
    temp = list(string.ascii_letters)
    random.shuffle(temp)
    return ''.join(temp)


class ListXTest(unittest.TestCase):

    def setUp(self):
        """
        make root directory to conduct
        tests with checking os.listdir
        output with expected output. most
        checks here are redundant as os.listdir
        is essentially covered by cpython's
        more-than-competent testing suite
        """

        # name and create root directory
        self.root_directory = 'lsx_root_dir'
        os.mkdir(self.root_directory)

        # generate random file names
        # and create them in self.root_directory
        self.file_names = [random_string() for _ in range(5)]
        for file_name in self.file_names:
            pathlib.Path(full_path(self.root_directory, file_name)).touch()

        # generate random directory names
        # and create them in self.root_directory
        self.dir_names = [random_string() for _ in range(5)]
        for dir_name in self.dir_names:
            os.mkdir(full_path(self.root_directory, dir_name))

    def test_files_check(self):

        before_lsx_files = os.listdir(self.root_directory)

        # basic redundant check
        self.assertEqual(before_lsx_files, lsx(self.root_directory))

        # create a file and then check
        pathlib.Path(full_path(self.root_directory, 'test_1.txt')).touch()
        self.assertEqual(
            sorted(before_lsx_files + ['test_1.txt']), sorted(lsx(self.root_directory))
        )

    def tearDown(self):
        shutil.rmtree(self.root_directory)
