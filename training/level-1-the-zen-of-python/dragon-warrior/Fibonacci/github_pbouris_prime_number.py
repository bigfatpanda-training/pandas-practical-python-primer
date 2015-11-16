
def 10001_prime_num():

   num_range = 200000
   prime_count = 0

   # check for factors

   for each_num in range(1, num_range):
       if each_num > 1:
           for each_range_num in range(2, each_num):
               if (each_num % each_range_num) == 0:
                   break
           else:
               prime_count += 1
               if prime_count == 10001:
                   print ("The 10,001st prime number is:" + str(each_num))
                   break
10001_prime_num()
