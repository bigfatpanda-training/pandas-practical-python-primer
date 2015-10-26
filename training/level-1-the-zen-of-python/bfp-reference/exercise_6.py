"""
Demonstrate the time/space performance differences between lists and tuples.
"""
import sys
import timeit


def iterate(test_object):
    """Iterate over a given object.  Do nothing for each iteration."""
    for item in test_object:
        pass

test_tuple = tuple(range(500000))
test_list = list(range(500000))
test_set = set(range(500000))

print(sys.getsizeof(test_tuple))
print(sys.getsizeof(test_list))
print(sys.getsizeof(test_set))

print(
    timeit.timeit('iterate(test_tuple)',
                  setup="from __main__ import iterate, test_tuple, test_list",
                  number=1000))

print(
    timeit.timeit('iterate(test_list)',
                  setup="from __main__ import iterate, test_tuple, test_list",
                  number=1000))

print(
    timeit.timeit('iterate(test_set)',
                  setup="from __main__ import iterate, test_tuple, test_list, test_set",
                  number=1000))