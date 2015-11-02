"""
Generates Prime Numbers
"""


class PrimeGenerator(object):
    def __init__(self):
        """
        Initialize the list of prime numbers.
        """

        self._prime_list = []

    def find_prime(self, nth_value):
        """
        Find the nth_value prime number.

        Args:
            nth_value: the nth_value to find

        Returns:
            The nth Prime Number as an int
        """
        index = 1
        while len(self._prime_list) < nth_value:
            index += 1
            if self._is_prime(index):
                self._prime_list.append(index)

        return self._prime_list[-1]

    def _is_prime(self, index):
        result = True

        for prime in self._prime_list:
            try:
                if index % prime == 0:
                    result = False
                    break
            except ZeroDivisionError:
                break;

        return result
