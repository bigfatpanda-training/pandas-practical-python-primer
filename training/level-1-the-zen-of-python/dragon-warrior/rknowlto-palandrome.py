multipliers = range(999, 99, -1)
greatest_product = 0
index = -1

for x in multipliers:
    index += 1

    for y in multipliers[index:]:
        product = x*y

        if (str(product) == str(product)[::-1]) and (product > greatest_product):
            greatest_product = product

print (greatest_product)
