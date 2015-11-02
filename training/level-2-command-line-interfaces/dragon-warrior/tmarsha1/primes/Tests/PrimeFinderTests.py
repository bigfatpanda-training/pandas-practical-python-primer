"""
Test the Prime Finder class

Still working on getting dependency injection working.
"""

import unittest
from primes.Primes import PrimeFinder
#from primes.Primes import PrimeGenerator

class PrimeFinderTests(unittest.TestCase):
    def test_find_prime(self):
        prime_finder = PrimeFinder.PrimeFinder(PrimeGenerator.PrimeGenerator())
        self.assertEqual(prime_finder.find_prime(6), 13)
