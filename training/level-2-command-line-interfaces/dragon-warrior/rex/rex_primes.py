import pprint

def Test(curr):
    t = False
    for prime in primes:
        if curr % prime == 0:
            t = True
            break
    return t

pprint.pprint('starting...')
primes = []
current =2
last = 10001

while not primes or len(primes)<last:
    if Test(current) == False:
        primes.append(current)
    current += 1
# pprint.pprint(primes)
pprint.pprint('10,001st prime is:')
pprint.pprint(primes[last-1])