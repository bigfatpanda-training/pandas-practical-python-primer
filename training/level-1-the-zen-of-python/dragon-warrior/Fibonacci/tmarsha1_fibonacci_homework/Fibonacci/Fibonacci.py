__author__ = 'tmarsha1'

class Fibonacci(object):
    def __init__(self, max_value:int):
        self.sequence = [1]
        self.fill_sequence(max_value)


    def fill_sequence(self, max_value:int):
        if max_value <= 0:
            raise ValueError('Invalid fibonacci sequence requested.')

        two_previous = 0
        one_previous = 1
        while True:
            current = two_previous + one_previous
            if (current > max_value):
                break

            self.sequence.append(current)
            two_previous = one_previous
            one_previous = current


    def __str__(self) -> str:
        return str(self.sequence)


    def sum(self) -> int:
        result = 0
        for item in self.sequence:
            result += item
        return result