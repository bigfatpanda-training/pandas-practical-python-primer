palindrome_List = []

Min_Product_Of_Three_Digit_Num = 100 ** 2

Max_Product_Of_Three_Digit_Num = 999 ** 2

for each_num in range(Min_Product_Of_Three_Digit_Num, Max_Product_Of_Three_Digit_Num + 1):
    if str(each_num) == str(each_num)[::-1]:
        palindrome_List.append (each_num)

print (max(palindrome_List))


