bfp = "You're just a big, fat panda! No, I am THE big, fat panda!"

print(bfp.count("fat"))

# Both find and index return index values but index returns an exception
# when the requested value is not found.
print(bfp.find("panda"))
print(bfp.index("panda"))

print(bfp.find("no panda"))
try:
    print(bfp.index("no panda"))
except ValueError as error:
    print(error)

# Create opposite case copy and determine three ways to test case-less equality.
bfp_2 = bfp.swapcase()
print(bfp == bfp_2)
print(bfp.lower() == bfp_2.lower())
print(bfp.upper() == bfp_2.upper())
print(bfp.casefold() == bfp_2.casefold())

# Partition
print(bfp.partition("!"))
print(bfp.partition("!")[2])  # Just get the part that you want.

# Split
print(bfp.split())
print(bfp.split(','))

# Use split and join to break apart and reconstitute string.
split_string = bfp.split()
rejoined_string = " ".join(split_string)
print(rejoined_string)





