"""
This code (which finds the sume of all unique multiples of 3/5 within a
given limit) breaks a significant number of PEP8 rules.  Maybe it doesn't even
work at all.

Find and fix all the PEP8 errors.
"""
import os, sys, operator

INTERESTEDMULTIPLES = [3, 5] # Incorrect constant syntax.
# Missing should have 2 blank lines between top-level functions.
def quickerMultipleOfThreeAndFive(top_limit): # Improperly named function.
    multiplier = 1
    multiples  = set()  # More than one space in an assignment.

    while True:
        if multiplier * 5 < top_limit: multiples.add(multiplier * 5) # Multiple statements on the same line.
        if multiplier * 3 < top_limit:
            multiples.add(multiplier * 3)
        else:
        break # Broken indentation.

        multiplier += 1

    return sum(multiples)

print("The sum of all unique multiples of 3 and 5 which given an upper limit of X is to consider is: answer")  # Over 80 Line Length
