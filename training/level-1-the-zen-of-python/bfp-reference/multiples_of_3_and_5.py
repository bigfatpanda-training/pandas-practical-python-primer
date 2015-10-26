"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


# Only Add Known Multiples, but still O(n)
def quicker_multiples_of_3_and_5(top_limit):
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

# Brute Force O(n)
def multiples_of_3_and_5(upper_limit):
    multiples = set()
    for possible_multiple in range(upper_limit):
        if not all([possible_multiple % 3, possible_multiple % 5]):
            multiples.add(possible_multiple)

    return sum(multiples)

    # print(sum(multiples))

if __name__ == '__main__':
    import timeit
    print(timeit.repeat("multiples_of_3_and_5(10000)",
                        setup="from __main__ import multiples_of_3_and_5",
                        number=1000, repeat=3))

    print(timeit.repeat("quicker_multiples_of_3_and_5(10000)",
                        setup="from __main__ import quicker_multiples_of_3_and_5",
                        number=1000, repeat=3))





