# Program C1: finding the smallest value

smallest_so_far = None
lst = [9, 41, 12, 3, 74, 15]
print(lst)
print('Before', smallest_so_far)
for the_num in lst:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After, the minimum value is', smallest_so_far)
#end
