"""
Prime - Print the Nth prime element

A simple factoring brute force algorithm to test and generate prime numbers.

Optimizations check only odd number candidates and only prime factors up to the
sqrt of the candidate.
"""

def is_prime(primes: list, candidate: int) -> bool:
    """
    Check if a number in a sequence is a prime number.

    Args:
        primes: A list of prime numbers.
        candidate: A int to check for potential primy-ness

    Returns:
        A bool indicating if candidate is a prime number.
    """

    prime = True
    i = 0
    while primes[i] <= candidate**0.5 and prime:
        prime = bool(candidate % primes[i])
        i += 1

    return prime


# Generate a list of prime numbers to specified length.

def prime_list(listLength):
    if listLength < 1 :
        return []

    primes = [2]
    candidate = 3
    while listLength > len(primes):
        if is_prime(primes, candidate):
            primes.append(candidate)
        candidate += 2

    return primes


if __name__ == "__main__":
    the_prime_which_i_seek = 10001
    primes=prime_list(the_prime_which_i_seek)

    #print(primes)
    print('The',the_prime_which_i_seek ,'Nth prime element is', primes[-1])