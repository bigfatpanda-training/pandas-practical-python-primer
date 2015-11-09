__author__ = 'tmarsha1'

import unittest

from Fibonacci import BruteForceEvenValueFibonacci


class Brute_Force_Fibonacci_Tests(unittest.TestCase):
    def test_sum(self):
        fib = BruteForceEvenValueFibonacci.BruteForceEvenValueFibonacci(20)
        self.assertEqual(fib.sum(), 10)