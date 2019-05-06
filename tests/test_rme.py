"""
unit tests for rme script
"""
import os
import shutil
import random
import pathlib
import unittest

from betterx import rme, full_path


class RemoveExceptTest(unittest.TestCase):
 
    def setUp(self):
        """
        make root directory to conduct
        tests with test directories and file
        assertions will be checked by different
        output from os.listdir against results
        from betterx.rme and known output
        """

        # name and create root directory
        self.root_directory = 'rme_root_dir'
        os.mkdir(self.root_directory)

        # name and create files in root directory
        self.file_names = ['profile.txt', 'posts.json', 'important.md']
        for file_name in self.file_names:
            pathlib.Path(full_path(self.root_directory, file_name)).touch()

        # name and create directories in root directory
        self.directory_names = ['projects', 'topics', 'research']
        for directory_name in self.directory_names:
            os.mkdir(full_path(self.root_directory, directory_name))

        # create files in existing directories for some test cases
        self.sub_dir_name = random.choice(self.directory_names)
        self.sub_file_names = ['sub_politics.txt', 'sub_texts.ini']
        for sub_file_name in self.sub_file_names:
            pathlib.Path(
                full_path(self.root_directory, sub_file_name, self.sub_dir_name)
            ).touch()

        # create directory to populate and test deletion later
        self.sub_dir_to_delete = 'users'
        os.mkdir(full_path(self.root_directory, self.sub_dir_to_delete))
        for index in range(1, 10):
            pathlib.Path(
                full_path(
                    self.root_directory, '{}.txt'.format(index), self.sub_dir_to_delete
                )
            ).touch()

    def test_rme_save_posts(self):
        """
        delete all files in self.root_directory
        except for posts.json and the sub
        """

        before_rme_files = os.listdir(self.root_directory)

        expected_files = [self.file_names[1], self.sub_dir_name, self.sub_dir_to_delete]

        rme(
            [self.file_names[1], self.sub_dir_name, self.sub_dir_to_delete],
            self.root_directory,
        )

        after_rme_files = sorted(os.listdir(self.root_directory))
        self.assertEqual(after_rme_files, expected_files)

    def test_rme_save_sub_politics(self):
        """
        delete all files in self.sub_dir_name
        except for "sub_politics.txt" and check
        """

        path = '{}/{}/'.format(self.root_directory, self.sub_dir_name)

        before_rme_files = os.listdir(path)

        # expected files in this case
        # is fairly easy to predict since
        # only 2 files exist so I don't
        # to go through all the hassle of
        # predicting all the files like
        # in the test_rme_save_posts test
        expected_files = [self.sub_file_names[0]]

        rme([self.sub_file_names[0]], path)

        after_rme_files = os.listdir(path)
        self.assertEqual(after_rme_files, expected_files)

    def test_rme_delete_populated_dir(self):

        before_rme_files = os.listdir(self.root_directory)
        expected_files = sorted([self.file_names[1], self.sub_dir_name])

        rme([self.sub_dir_name, self.file_names[1]], self.root_directory)

        after_rme_files = sorted(os.listdir(self.root_directory))
        self.assertEqual(after_rme_files, expected_files)

    def test_rme_supress_FileNotFound(self):

        self.assertRaises(
            FileNotFoundError, rme, 'does_not_exist.md', self.root_directory
        )

    def tearDown(self):
        shutil.rmtree(self.root_directory)
