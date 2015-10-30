__author__ = 'tmarsha1'

import unittest

from Fibonacci import OptimizedEvenValueFibonacci


class OptimizedEvenValueFibonacci_Tests(unittest.TestCase):
    def test_sum(self):
        fib = OptimizedEvenValueFibonacci.OptimizedEvenValueFibonacci(20)
        self.assertEqual(fib.sum(), 10)