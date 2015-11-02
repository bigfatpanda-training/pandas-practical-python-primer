print('hello')
x1=1
x2=1
x3 = 0
tally=0
while(x3<4000):
    x3=x1+x2
    if(x3 % 2 ==0):
        tally = tally + x3
    print(x3,", ",tally)
    x1=x2
    x2=x3
