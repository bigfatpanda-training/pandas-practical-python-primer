# Reassign the name 'my_cool_list' to a new list() object.
my_cool_list = list()

# At at least five elements to it.
my_cool_list.append(1)
my_cool_list.append(5)
my_cool_list.append(2)
my_cool_list.append(4)
my_cool_list.append(3)

# Access elements by index
my_cool_list[0]
my_cool_list[2]
my_cool_list[4]

# Rearrange the elements of the list
my_cool_list.reverse()
print(my_cool_list)
my_cool_list.sort()  # What about the optional parameters?
print(my_cool_list)

# Figure out how to remove elements from the list.
# clear: removes all elements
# pop: removes and returns an element at given index (default last)
# remove: removes the first occurrence of a given value in the list.
my_cool_list.pop(3)
print(my_cool_list)
my_cool_list.remove(5)
print(my_cool_list)
my_cool_list.clear()
print(my_cool_list)
