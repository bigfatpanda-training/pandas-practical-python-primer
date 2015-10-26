__author__ = 'jsmith68'
sum = 0
f1, f2 = 0, 1
while f2 < 4000000:
    if f2 % 2 == 0:
        sum+= f2
    f1,f2 = f2, f1 + f2
print (sum)