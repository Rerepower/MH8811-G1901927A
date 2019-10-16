#import json
#import pickle

#def my_serialize(my_list):
  #  f = open("a.txt", 'w', encoding='utf-8')

   # json.dump(my_list, f, ensure_ascii=False)
    #f.close()    

#def my_deserialize():

# input a list consisted with integer
# try block to handle the exception 
#try: 
  #  my_list = [] 
 #   while True: 
   #     my_list.append(int(input())) 
#except: 
    #print("Invalid input, please input an integer.") 
#------------------------------------
lst = [1, 2, 3, 4, 5]

def serialize(l):
    res = ''
    for i in l :
        res = res + str(i)
        res = res + ';'
    return res[:-1]
# not work with empty list , find a way to solve it
def deserialize(s) :
    lst_of_str = s.split(';')
    res = list()
    for string in lst_of_str :
        res.append(int(string))
    return res

# input lst from user
serialized = serialize(lst)
print(serialized)
# write to file
# read from file
lst2 = deserialize(serialized)

print(lst)
print(lst2)