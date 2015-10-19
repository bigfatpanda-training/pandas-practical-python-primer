"""
This code (which finds the sum of all unique multiples of 3/5 within a
given limit) breaks a significant number of PEP8 rules.  Maybe it doesn't even
work at all.

Find and fix all the PEP8 errors.
"""
import os
import sys
import operator

INTERESTED_MULTIPLES = [3, 5]


def quicker_multiple_of_three_and_five(top_limit):
    multiplier = 1
    multiples = set()

    while True:
        if multiplier * 5 < top_limit:
            multiples.add(multiplier * 5)
        if multiplier * 3 < top_limit:
            multiples.add(multiplier * 3)
        else:
            break

        multiplier += 1

    return sum(multiples)


print("The sum of all unique multiples of 3 and 5 which given an "
      "upper limit of X is to consider is: answer")
