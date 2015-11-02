__author__ = 'tmarsha1'

from Fibonacci import Fibonacci


class BruteForceEvenValueFibonacci(Fibonacci.Fibonacci):
    def sum(self)->int:
        result = 0
        for item in self.sequence:
            if item % 2 == 0:
                result += item
        return result
