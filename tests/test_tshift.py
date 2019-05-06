"""
unit tests for tshift script
"""
import os
import sys
import shutil
import unittest

from betterx import tshift, full_path

text_tab_1 = """#!/usr/bin/env python3
def main():
	if 2 > 1:
		print('2 is greater')
	else:
		print('the end is near')

if __name__ == '__main__':
	main()
"""

text_tab_2 = """zzz
			aaa
		bbb
	ccc
	eee
		qqq
"""

text_tab_3 = """222
333
	444	7
	11	555
	9999	77
		88	9
"""

text_space_1 = """#!/usr/bin/env python3
def main():
    if 2 > 1:
        print('2 is greater')
    else:
        print('the end is near')

if __name__ == '__main__':
    main()
"""

text_space_2 = """zzz
         aaa
      bbb
   ccc
   eee
      qqq
"""

text_tab_3 = """222
333
      444      7
      11      555
      9999      77
            88      9
"""


class TabShiftTest(unittest.TestCase):
    def setUp(self):
        """
        create files for testing
        and compare them to results of 
        """

        self.root_directory = 'tshift_root_dir'
        os.mkdir(self.root_directory)

        self.files = ('test_1.py', 'test_2.txt', 'test_3.txt')

        with open(full_path(self.root_directory, 'test_1.py'), 'w+') as f:
            f.write(text_tab_1)
            f.close()

        with open(full_path(self.root_directory, 'test_2.txt'), 'w+') as f:
            f.write(text_tab_2)
            f.close()

        with open(full_path(self.root_directory, 'test_3.txt'), 'w+') as f:
            f.write(text_tab_3)
            f.close()

    def test_text_tab_1_to_space(self):

        path = full_path(self.root_directory, self.files[0])
        tshift(path)
        after_tshift_file = open(path)
        after_tshift_text = after_tshift_file.read()
        after_tshift_file.close()
        self.assertEqual(after_tshift_text, text_space_1)

    def test_text_tab_2_to_space(self):

        path = full_path(self.root_directory, self.files[1])
        tshift(path, 3)
        after_tshift_file = open(path)
        after_tshift_text = after_tshift_file.read()
        after_tshift_file.close()
        self.assertEqual(after_tshift_text, text_space_2)

    def test_text_tab_3_to_space_with_listdir(self):

        before_tshift_files = os.listdir(self.root_directory)
        expected_files = sorted(
            os.listdir(self.root_directory) + ['post_tshift_test_3.txt']
        )

        path = full_path(self.root_directory, self.files[2])
        tshift(path, 6, full_path(self.root_directory, 'post_tshift_test_3.txt'))

        after_tshift_files = sorted(os.listdir(self.root_directory))
        self.assertEqual(after_tshift_files, expected_files)

    def test_file_exist_fail(self):

        success, error = tshift(full_path(self.root_directory, 'test_4.txt'))
        self.assertFalse(success)
        self.assertRegex(error, r"file ([\"'])(?:(?=(\\?))\2.)*?\1 does not exist")

    def test_negative_space_number_fail(self):

        success, error = tshift(full_path(self.root_directory, self.files[1]), -2)
        self.assertFalse(success)
        self.assertEqual('space number should be a non zero positive number', error)

    def tearDown(self):
        shutil.rmtree(self.root_directory)
