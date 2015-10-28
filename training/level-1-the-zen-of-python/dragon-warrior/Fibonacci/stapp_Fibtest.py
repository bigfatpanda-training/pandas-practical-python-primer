"""
Compute Fibonacci sequence and learn python.
Steve Tapp
"""
import sys
import timeit

fib_seq = [0, 1]
fib_even_sum = 0

for fibnum in range (2, 50):
    fib_seq.append(fib_seq[-2] + fib_seq[-1])
    print (fibnum, fib_seq[fibnum])
    if fib_seq[-1] >= 4000000:
        break
    if not fib_seq[fibnum] % 2:
        print ('even', fib_seq[fibnum])
        fib_even_sum += fib_seq[fibnum]

print ('Sum of even fibonacci terms under 4 million is ', fib_even_sum)
