my_cool_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get Specific Index Positions
print(my_cool_list[0])
print(my_cool_list[2])

# With Negative Numbers Too
print(my_cool_list[-1])
print(my_cool_list[-10])

# Total Element Count
print(len(my_cool_list))

# Smallest Element
print(min(my_cool_list))

# Largest Element
print(max(my_cool_list))

my_cool_list.append("String to mess stuff up.")

try:
    print(min(my_cool_list))
    print(max(my_cool_list))
except TypeError:
    my_cool_list.pop()


# Specify a step of 2, 3, 4
print(my_cool_list[0:6:2])
print(my_cool_list[0:6:3])
print(my_cool_list[0:6:4])
