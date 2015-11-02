__author__ = 'tmarsha1'

from Fibonacci import Fibonacci
from Fibonacci import BruteForceEvenValueFibonacci
from Fibonacci import OptimizedEvenValueFibonacci

if __name__ == '__main__':
    max_value = 4000000

    fibonacci = Fibonacci.Fibonacci(max_value)
    print("Sum of fibonacci values: %s" % '{:,}'.format(fibonacci.sum()))

    fibonacci = BruteForceEvenValueFibonacci.BruteForceEvenValueFibonacci(max_value)
    print("Sum of brute force even values: %s" % '{:,}'.format(fibonacci.sum()))

    fibonacci = OptimizedEvenValueFibonacci.OptimizedEvenValueFibonacci(max_value)
    print("Sum of optimized even values: %s" % '{:,}'.format(fibonacci.sum()))