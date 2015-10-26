first_number = 1
second_number = 2
third_number = 3

running_total = 2   # Seeding with 2 because it is the first even number and not included in the while loop


def is_even_number(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


while third_number <= 4000000:
    if is_even_number(third_number):
        running_total += third_number

    first_number = second_number
    second_number = third_number
    third_number = first_number + second_number

print("Total")
print(running_total)
