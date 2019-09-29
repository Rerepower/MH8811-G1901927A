# 3rd Homework
# Design a program with 3 sub-program given users choices to run "Hello, world" -
# - Personlized hello world and Celsius to Fahrenheit convert program with loop and exit function
# Define Hello world Function
def func_hello_world():
    print("Hello, world!")
#----------------------------------------------------#
# Define User's Hello world function
def func_user_hello_world():
    username = input("Please input your name: ")
    print('Hello, ',username,' !')
#----------------------------------------------------#
# Define Celsius to Fahrenheit convert function
def func_temp_convert():
    # Ask user to put number in case he or she enters a character
    while True:
        try:
            str_num = input('Please enter a temperature in Celsius: ')
            celsius = float(str_num)
            break
        except:
            print('Incorrect input, please enter a NUMBER in Celsius!')
    fahrenheit = celsius * 1.8 +  32
    print(str(celsius) + ' Celsius in Fahrenheit is ' + str(fahrenheit))
#----------------------------------------------------#
# Sub-program loop
while True:
    print('Choose the program you would like to run: \n Press 1 for printing "Hello, World!" \n Press 2 for Personalized Hello World \n Press 3 for Celsius to Fahrenheit Converter \n Press other keys to exit')
    x = input()
    if x == str(1):
        func_hello_world()
        continue
    if x == str(2):
        func_user_hello_world()
        continue
    if x == str(3):
        func_temp_convert()
        continue
    else:
        break
print('Thanks for using my program!')
#end