"""
Test the Prime Finder class

Still working on getting dependency injection working.
Injecting the Generator into the Finder allows for many possibilities.
From the testing perspective this would allow me to inject a mock object
for the Generator that returns a set value speeding up the testing of the
Prime Finder class.
"""

import unittest
from primes.Primes import PrimeFinder
#from primes.Primes import PrimeGenerator

class PrimeFinderTests(unittest.TestCase):
    def test_find_prime(self):
        prime_finder = PrimeFinder.PrimeFinder(PrimeGenerator.PrimeGenerator())
        self.assertEqual(prime_finder.find_prime(6), 13)
