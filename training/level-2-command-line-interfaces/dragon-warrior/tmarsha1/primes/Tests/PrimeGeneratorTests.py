"""
Test the Prime Generator class
"""

import unittest
from primes.Primes import PrimeGenerator

class PrimeGeneratorTests(unittest.TestCase):
    def test_find_prime(self):
        prime = PrimeGenerator.PrimeGenerator()
        self.assertEqual(prime.find_prime(6), 13)

    def test_find_answer(self):
        prime = PrimeGenerator.PrimeGenerator()
        self.assertEqual(prime.find_prime(10001), 104743)