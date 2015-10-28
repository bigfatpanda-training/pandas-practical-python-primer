__author__ = 'twilson2'

def fibadd(a, b, c):
    c = a + b

f1 = 1
f2 = 2
f3 = f1 + f2
f4 = 0
while f2 <= 4000000:
    if f2 % 2 == 0:
        print("f2:" ,f2)
        #f4 = f4 + f2
        fibadd(f4, f2, f4)
    f1 = f2
    f2 = f3
    f3 = f1 + f2

print("Sum of Even Fibbonaci Numbers Less Than 4,000,000: ",f4)