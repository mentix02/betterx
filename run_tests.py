#!/usr/bin/env python3
import unittest

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_runner = unittest.TextTestRunner()
    ftest_suite = test_loader.discover('tests')
    test_runner.run(ftest_suite)
