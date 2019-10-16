# 05_H1 Serialization with types
# import json library
import json
#---------------------------------------
# Define function to open file
def my_openfile(fname):
    fhandle = open(fname)
    data = json.load(fhandle)
    fhandle.close()
    return data
#----------------------------------------
# Define serializer function
def my_serializer(ld):
    my_string = json.dumps(ld)
    return my_string
#----------------------------------------
# Combine compare with list and dict
def my_compare(d1,d2):
    if type(d1) == type(d2):
        if type(d1) == type([]):
            print(comlist(d1,d2))
        if type(d1) == type({}):
            print(comdict(d1,d2))
    else:
        print('FALSE')
#----------------------------------------
# Define function to compare list
def comlist(d1,d2):
    if d1 == d2:
        return True
    else:
        return False
#----------------------------------------
# Define function to compare dictionary
def comdict(d1,d2):
    if d1 != {} and d2 != {}:
        for i in d1 and d2 :
            if not d1[i] == d2[i]:
                return False
            elif not d1 == d2:
                return False
    elif d1 == d2:
        return True
    else:
        return False
#----------------------------------------
# Open the file to load data
d1 = my_openfile(input('Please input the file name you want to open: '))
print(d1)
#----------------------------------------
# Serialize the data into string in the file
serialized_file = my_serializer(d1)
print(type(serialized_file))
#----------------------------------------
# Save the string into the file
savefile = input("What is the new file's name： ")
with open(savefile,'w') as file1:
    json.dump(serialized_file,file1)
    file1.close()
#----------------------------------------
# Read string
with open(savefile) as file2:
       d2=json.load(file2)
       file2.close()
print(d2)
#----------------------------------------
# Deserialize
d2 = json.loads(d2)
print(d2)
#----------------------------------------
# Compare
my_compare(d1,d2)