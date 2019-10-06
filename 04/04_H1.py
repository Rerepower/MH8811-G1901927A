# Calculate the sample variance for the dataset

# Define getFileLines function
def getFileLines(fname) :
    fhandle = open(fname)
    lines = []
    for line in fhandle :
        line = line.rstrip()
        if line :
            lines.append(line)
    fhandle.close()
    return lines

# Define average function
def myaverage(lst):
    count = 0
    sum = 0
    for value in lst:
        count = count + 1
        sum = sum + value
    average_num = sum / count
    return average_num

# Define sample variance funtion
def myVariance(lst) :
    sumDiff = 0
    count = 0
    for i in range(0, len(lst)) :
        sumDiff = sumDiff + ((lst[i] - myaverage(lst)) ** 2)
        count = count + 1
    my_variance = sumDiff / (count - 1)
    return my_variance

# Import files
lst = getFileLines('Data.csv')

# Convert each element of lst into int type
for i in range(0, len(lst)) :
    lst[i] = int(lst[i])

# Call functions
print('Sample Variance is', myVariance(lst))
#end