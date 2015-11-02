"""
Homework 3 find the 10,001st prime number
increment a set of numbers
for each number, determine if it is a prime number
-build a
- if the number is mod 2, throw it out
- if the number is mod 3, throw it out
- if the number is mod 5...
build a list of prime numbers


"""

def is_prime(n : int):
    """

    Determine if the integer is prime

    """
    prime = 0
    print ("n = ",n)
    if n <= 1:
        prime = 0
        print("prime1: ",prime)
    elif n <= 3:
        prime = 1
        print("prime2: ",prime)
    elif (n % 2 == 0 or n % 3 == 0):
        prime = 0
        print("prime3: ",prime)
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            prime = 0
        i = i + 1
        prime = 1
    print("prime4: ",prime)


prime_list = [2]      # tracks the list of prime numbers
counter = 2           # tracks the number to be evaluated as prime
prime_counter = 0     # tracks the number of primes, stop when this hits 10,000 (since it starts at 0)
n = 0

while n < 10:
    possible_prime = is_prime(n)
    print ("is prime? ", possible_prime)
    n = n + 1

