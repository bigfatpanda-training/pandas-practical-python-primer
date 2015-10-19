#__author__ = 'twilson2'
x_range = range(900,1000)
y_range = range(900,1000)

#
print(len(x_range))
print(min(x_range))
print(max(x_range))
#print(x_range[300])
#print(x_range.count(300))
#print(x_range.index(300))

for x_num in x_range:
    for y_num in y_range:
        z_num = (x_num * y_num)
        z_list = list(map(int, str(z_num)))
        #print(len(z_list))
        #need to get len of list to determine if I have to iterate an odd or even number of digits
        #need an if elif construct for the evens/odds
        #how do I iterate with variables and not hardcoded index values? and a while loop?
        #then I have to .append my values into a palindrome array to hold them.
        #then determine the largest palindrome
        if len(z_list) % 2 == 0:  # this not necessary since I changed the start of range from 100 to 900
            if z_list[0] == z_list[-1]:
                if z_list[1] == z_list[-2]:
                    if z_list[2] == z_list[-3]:
                        print(z_list, z_list[0], z_list[-1], z_list[1], z_list[-2])


