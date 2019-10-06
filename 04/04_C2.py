# Basic Descriptive Statistics
mylist = [9, 41, 12 ,3, 74, 15]
#-------------------------------------------------
# Define min function
def mymin(lst):
    smallest_so_far = None
    for the_num in lst :
        if smallest_so_far is None:
            smallest_so_far = the_num
        elif the_num < smallest_so_far:
            smallest_so_far = the_num
    return smallest_so_far
#-------------------------------------------------
# Define max function
def mymax(lst):
    largest_so_far = None
    for the_num in lst:
        if largest_so_far is None :
            largest_so_far = the_num
        elif the_num > largest_so_far : 
            largest_so_far = the_num 
    return largest_so_far
#-------------------------------------------------
# Define average function
def myaverage(lst):
    count = 0
    sum = 0
    for value in lst:
        count = count + 1
        sum = sum + value
    average_num = sum / count
    return average_num
#-------------------------------------------------
# Define median function
def mymedian(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        r = int(len(lst)/2)
        median_lst = lst[r]
    else:
        r = int((len(lst)-1)/2)
        median_lst = (lst[r]+lst[r+1]) / 2
    return median_lst
#-------------------------------------------------
# Define range function
def myrange(lst):
    range_lst = mymax(lst) - mymin(lst)
    return range_lst
#-------------------------------------------------
# Call functions
print(mylist)
print('Min is', mymin(mylist))
print('Max is', mymax(mylist))
print('Average is', myaverage(mylist))
print('Median is', mymedian(mylist))
print('Range is', myrange(mylist))
#end
#-------------------------------------------------