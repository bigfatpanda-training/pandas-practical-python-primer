__author__ = 'tmarsha1'

from Fibonacci import Fibonacci


class OptimizedEvenValueFibonacci(Fibonacci.Fibonacci):
    def __init__(self, max_value:int):
        super(OptimizedEvenValueFibonacci, self).__init__(max_value)
        self.sequence = self.sequence[2::3]


    def sum(self)->int:
        result = 0
        for item in self.sequence:
            result += item
        return result