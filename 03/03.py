# 3rd Homework
# Design a program with 3 sub-program given users to run "Hello, world" -
# - Personlized hello world and Celsius to Fahrenheit convert program with loop and exit function
# Define Hello world Function
def funcHelloWorld():
    print("Hello, world!")
#----------------------------------------------------#
# Define User's Hello world function
def funcUserHelloWorld():
    username=input("Please input your name: ")
    print('Hello, ',username,' !')
#----------------------------------------------------#
# Define Celsius to Fahrenheit convert function
def funcTempConvert():
    # Ask user to put number in case he or she enters a character
    while True:
        try:
            str_num = input('Please enter a temperature in Celsius: ')
            Celsius=float(str_num)
            break
        except:
            print('Incorrect input, please enter a NUMBER in Celsius!')
    Fahrenheit=Celsius*1.8+32
    print(str(Celsius) + ' Celsius in Fahrenheit is ' + str(Fahrenheit))
#----------------------------------------------------#
# Sub-program loop
while True:
    print('Choose the program you would like to run: \n Press 1 for printing "Hello, World!" \n Press 2 for Personalized Hello World \n Press 3 for Celsius to Fahrenheit Converter \n Press other keys to exit')
    x = input()
    if x == str(1):
        funcHelloWorld()
        continue
    if x == str(2):
        funcUserHelloWorld()
        continue
    if x == str(3):
        funcTempConvert()
        continue
    else:
        break
print('Thanks for using my program!')
#end
