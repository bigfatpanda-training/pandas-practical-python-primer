"""
Attempt to inject the Prime Generator into the Prime Finder class.

At this point, I need to do more research to accomplish this.
"""


from primes.Primes import PrimeGenerator

class PrimeGenerator(object):
    def __init__(self, prime_generator):
        self._prime_generator = prime_generator

    def find_prime(self, nth_value):
        return self._prime_generator.find_prime(nth_value)
