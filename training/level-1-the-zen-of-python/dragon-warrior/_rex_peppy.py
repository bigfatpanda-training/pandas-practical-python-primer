"""
This code (which finds the sume of all unique multiples of 3/5 within a
given limit) breaks a significant number of PEP8 rules.  Maybe it doesn't even
work at all.

Find and fix all the PEP8 errors.
"""
import os
import sys
import operator

InterestedMultiples = [3, 5]

def quickerMultipleOfThreeAndFive(top_limit):
    multiplier = 1
    multiples  = set()

    while True:
        if multiplier * 5 < top_limit:
            multiples.add(multiplier * 5)
        if multiplier * 3 < top_limit:
            multiples.add(multiplier * 3)
        else:
        break

        multiplier += 1

    val = sum(multiples)
    return val

print("The sum of all unique multiples of 3 and 5 which given an upper limit of X is to consider is: answer")
