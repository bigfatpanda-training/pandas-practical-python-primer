__author__ = 'tmarsha1'

import unittest
from Fibonacci import Fibonacci


class FibonacciTests(unittest.TestCase):
    def test_sequence(self):
        fib = Fibonacci.Fibonacci(20)
        self.assertEqual("[1, 1, 2, 3, 5, 8, 13]", str(fib))

    def test_sum(self):
        fib = Fibonacci.Fibonacci(5)
        self.assertEqual(fib.sum(), 12)