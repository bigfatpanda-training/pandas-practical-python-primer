__author__ = 'tmarsha1'

import unittest

from palindrome.tmarsha1_palindrome_homework.homework import is_palindrome
from palindrome.tmarsha1_palindrome_homework.homework import brittle_palindrome_solution


class BrittlePalindromeSolutionTest(unittest.TestCase):
    def test_brittle_solution(self):
        self.assertEqual(brittle_palindrome_solution(), 906609)

    def test_true_numeric_is_palindrome(self):
        self.assertTrue(is_palindrome(906609))

    def test_false_numeric_is_palindrome(self):
        self.assertFalse(is_palindrome(123456))

    def test_true_string_is_palindrome(self):
        self.assertTrue(is_palindrome("mom"))

    def test_false_string_is_palindrome(self):
        self.assertFalse(is_palindrome("mother"))