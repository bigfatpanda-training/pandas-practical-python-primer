__author__ = 'tmarsha1'

""" find largest palindrome for the product of 2 three digit numbers
    (100-999) or (100^2 - 999^2)
    Answer is 913 * 993 = 906609
"""

import re

class Word(object):
    def __init__(self, values):
        concat = ""
        for value in values:
            concat = concat + self.format_value(value)
        self.concatenated_word = concat

    def format_value(self, value):
        value = str(value).lower()
        value = re.sub("[^A-Za-z0-9]", "", value)
        return value

    def is_palindrome(self):
        return self.concatenated_word == self.concatenated_word[::-1]

    def to_str(self):
        return self.concatenated_word


def is_palindrome(value):
    result = False
    value = str(value)
    if value == value[::-1]:
        result = True
    return result


def compare_palindromes(word1, word2):
    result = word1
    if int(word1.to_str()) < int(word2.to_str()):
        result = word2
    return result


def brittle_palindrome_solution(lower_bounds, upper_bounds):
    max_palindrome = Word("0")

    for first_item in range(lower_bounds, upper_bounds):
        for second_item in range(lower_bounds, upper_bounds):
            product = first_item * second_item
            word = Word(str(product))
            if word.is_palindrome():
                max_palindrome = compare_palindromes(max_palindrome, word)

    return max_palindrome


if __name__ == '__main__':
    print("palindrome: %s" % brittle_palindrome_solution(100, 1000).to_str())
