# This program says hello and asks for my name and age

print("Hello, What is your Name ? ")
my_name = input() # variable storing name
print("Hello , " + my_name)
print("The length Of your name is : " + str(len(my_name))) # len fn used to display the length of name
print("Please Enter Your age : ")
my_age = input() # variable storing age
print("You will be " + str(int(my_age) + 1) + " in a year.")