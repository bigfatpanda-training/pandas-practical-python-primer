__author__ = 'tmarsha1'

""" find largest palindrome for the product of 2 three digit numbers
    (100-999) or (100^2 - 999^2)
"""


def is_palindrome(value):
    result = False
    value = str(value)
    if value == value[::-1]:
        result = True
    return result


def brittle_palindrome_solution():
    LOWER_BOUNDS = 100
    UPPER_BOUNDS = 1000

    max_palindrome = 0

    for first_item in range(LOWER_BOUNDS, UPPER_BOUNDS):
        for second_item in range(LOWER_BOUNDS, UPPER_BOUNDS):
            product = first_item * second_item
            if is_palindrome(product):
                if max_palindrome < product:
                    max_palindrome = product

    return max_palindrome


if __name__ == '__main__':
    print("palindrome: %i" % brittle_palindrome_solution())