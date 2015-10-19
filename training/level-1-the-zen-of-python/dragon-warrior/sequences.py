test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (test_list[4])
# print (len(test_list))
# print (min(test_list))
# print (max(test_list))
# print (test_list.index(4))
# print (test_list.count(4))

test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print (test_tuple[4])

test_string = "Hello World"
# print (test_string[4])

test_range = range(100)
# print (test_range[4])

for x in test_range[-2:-8:-1]:
    print(x)

for x in test_range.__reversed__():
    print (x)
