"""
This module finds the n'th prime number and prints it out.
"""
import math

PRIME_TO_FIND = 10001


def is_prime(num: int) -> bool:
    if num > 0 and type(num) == int:
        factor_found = False

        if num == 2:
            factor_found = False
        else:
            for factor in range(2, math.ceil(math.sqrt(num))+1):
                if num % factor == 0:
                    factor_found = True
                    # print('Factor found: ',  factor)

        return not factor_found
    else:
        print('Number to test for prime must be a positive integer!')
        return False


def get_prime(prime_to_find: int) -> int:
    if prime_to_find > 0 and type(prime_to_find) == int:
        prime_numbers = 0
        current_number = 1  # Will increment in loop to start at 2

        while prime_numbers < prime_to_find:    # Get the n'th prime number
            current_number += 1

            # print('Current Number: ', current_number)

            if is_prime(current_number):
                prime_numbers += 1

        return current_number
    else:
        print('Prime number to find must be a positive integer!')
        return 0

print('Prime #', PRIME_TO_FIND, '=', get_prime(PRIME_TO_FIND))
