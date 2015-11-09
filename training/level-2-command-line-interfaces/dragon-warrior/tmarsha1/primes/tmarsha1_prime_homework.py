"""
Prime Number Homework
"""


from primes.Primes import PrimeGenerator

if __name__ == "__main__":
    primeToFind = 10001
    prime = PrimeGenerator.PrimeGenerator()
    primeValue = prime.find_prime(primeToFind)
    print("The %s prime number is %s" % ('{:,}'.format(primeToFind),
                                         '{:,}'.format(primeValue)))