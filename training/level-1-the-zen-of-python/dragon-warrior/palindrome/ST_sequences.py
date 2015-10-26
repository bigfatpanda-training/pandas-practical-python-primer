my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (my_list[2])
print(len(my_list))
print(min(my_list))
print(max(my_list))

test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(test_tuple[-4])

test_string = "mystring is here"
print(test_string)
print(list(test_string[-4:2]))

test_range = range(100)
print(list(test_range[8:66:-2]))

my_list.append('hello')
print(my_list)



print(my_list.count(4))

print(523 in test_range)

for number in test_range:
    if number == 5:
        print(number)
    else:
        print ("nope")
    pass

