"""This is a module to identify a specific prime number in sequence"""


_prime_list = [2, 3]


def is_prime_number(n:int) -> bool:
    """
    This function determines if the provided integer is a prime number. If so,
    it will add the number to the prime number list, and return that it is true
    that it is a prime number.

    Args:
        n: Number to determine whether it is prime.
    """

    i = 0
    is_prime = True

    if (n == 2 or n == 3):
        return True
    while(i < len(_prime_list)):
        if (not n % _prime_list[i] and is_prime):
            is_prime = False
            return is_prime
        i += 1
    if (is_prime):
        _prime_list.append(n)
    return is_prime


def prime_number(n: int) -> int:
    """
    This function returns the value of the prime number in sequence
    selected by the given integer argument.

    Args:
        n: Integer defining the prime number in sequence to return
    """

    count = 0
    number = 2
    while (count <= n):
        result = is_prime_number(number)
        if result:
            count += 1
        if (count == n):
            return number;
        number += 1


result = prime_number(10001)
print(result)
