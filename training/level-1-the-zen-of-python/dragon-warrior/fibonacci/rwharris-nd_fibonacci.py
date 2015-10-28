def even_fibonacci_sum(a:int,b:int,max:int) -> int:
    temp = 0
    sum = 0

    while (b <= max):
        if (b%2 == 0):
            sum += b
        temp = a + b
        a = b
        b = temp

    print(sum)

even_fibonacci_sum(1,2,4000000)