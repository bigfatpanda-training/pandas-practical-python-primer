#test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#test_string = "Example String blah"
#test_range = range(100)

#for item in test_range:
#    print(item)
#s=[]
# print(list(test_range[::-1]))
#for n1 in range(10,100):
#    for n2 in range(10,100):
#        n3 = n1*n2
#        print(n1," * ",n2," = ", n3)
#print(test_string[::2])
print('hello')
x1=1
x2=1
x3 = 0
tally=0
while(x3<4000000):
    x3=x1+x2
    if(x3 % 2 ==0):
        tally = tally + x3
        print(x3,", ",tally)
    x1=x2
    x2=x3
