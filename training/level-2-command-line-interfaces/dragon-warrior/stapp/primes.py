"""
Prime - Print the Nth prime element

A simple factoring brute force algorithm to test and generate prime numbers.

Optimizations check only odd number candidates and only prime factors up to the sqrt
of the candidate.
"""

# Steve Tapp 11/2/15


# Check if a number in a sequence is a prime number.

def isPrime (primes, candidate):
    prime = True
    i = 0
    while primes[i] <= candidate**0.5 and prime:
        prime = candidate % primes[i]
        i += 1

    return prime


# Generate a list of prime numbers to specified length.

def primeList(listLength):
    if listLength < 1 :
        return []

    primes = [2]
    candidate = 3
    while listLength > len(primes):
        if isPrime(primes, candidate):
            primes.append(candidate)
        candidate += 2

    return primes


# Main program

the_prime_which_i_seek = 10001
primes=primeList(the_prime_which_i_seek)

#print(primes)
print('The',the_prime_which_i_seek ,'Nth prime element is', primes[-1])