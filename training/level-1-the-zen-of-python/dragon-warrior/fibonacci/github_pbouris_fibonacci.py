
def fibonacci_funct():
    first_num, second_num = 0, 1
    sum_of_even_numbers = 0
    print (first_num)
    while second_num <= 4000000:
        if (second_num % 2) == 0:
            sum_of_even_numbers += second_num
        first_num, second_num = second_num, first_num + second_num

    print ("The sum of all even numbers in the Fibonacci sequence is equal to: " + str(sum_of_even_numbers))


myval = fibonacci_funct()