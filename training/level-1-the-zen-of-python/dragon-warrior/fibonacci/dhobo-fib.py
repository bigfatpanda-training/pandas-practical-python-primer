__author__ = 'jsmith68'
## Generate list of Fib Numbers

def fib():
    a, b = 0,1
    while True:
        yield a
        a,b = b, a + b

fibList = []
for index, fib_number in enumerate(fib()):
    if fib_number % 2 == 0:
        fibList.append(fib_number)
    if fib_number >= 4000000:
            break

#print(str(fibList).strip('[]'))
print(str(sum(fibList)))
