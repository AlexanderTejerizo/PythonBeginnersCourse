# # Lesson 1: Variables 
# fishFace = 1 camelCase
# print(fishFace)

# this_is_snake_case= 2 Snake case
# print(this_is_snake_case)

# re4l = 3 Number Variable
# print(re4l)

# #Data points
# Float_1 = 1.5
#                 #Floating Points
# Float_2 = 2.5

# Int_1 = 1
#                 #Integer
# Int_2 = 2

# Boolean_1 = True
#                 #Boolean
# Boolean_2 = False 

# print(Float_1)
# print(Float_2)
# print(Int_1)
# print(Int_2)
# print(Boolean_1)
# print(Boolean_2)

# # Number Operators
# Addition = 1 + 1
# Subtraction = 3 - 2
# Multiplication = 2 * 2
# Division = 10 / 2

# Exponentiation = 4 ** 4
# floorDevision = 10 // 3
# Modulo = 10 % 3

# # Assignments
# Addition += 5
# Subtraction -= 3
# Division /= 2.5

# print(Division)

# # Grocery Store Programming Challenge
# penne = 16.88
# Pasta_Sauce = 6.98
# olives = 16.76
# I_seasoning = 15.26
# baguettes = 3.00
# meatballs = 4.39

# subtotal = round(penne + Pasta_Sauce + olives + I_seasoning + baguettes + meatballs, 2)
# print(subtotal)

# # Strings Exercises
# to_slice = "Just do it!"
# print(to_slice[10])   # prints "!"
# print(to_slice[5:7])  # prints "do"
# print(to_slice[8:])   # prints "it!"
# print(to_slice[:4])   # prints "Just"
# print("Don't " + to_slice[5:])  # prints "Don't do it!"

# # type(), str(), and escape sequences exercises
# ex_b = True
# ex_i = 4
# ex_f = 4.123 # variable that has been assigned to a float
# print(type(ex_f)) # prints the type of float_num
# print(str(ex_f) + " is a float") # prints "6.7 is a float"

# print("\"Hello, my name is Alex, it's nice to meet you!\"") # prints "Hello, I'm Alex, it's nice to meet you"

# print("*******\n *****\n  ***\n   *") # prints an asterisk triangle


# # Input Programming challenge: Monty Python.
# name = input("What is your name?")
# quest = input("What is your quest?")
# color = input("what is your favorite color?")
# print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")


# int() exercise
# num = int(input("Please type and integer, it will be added with ten."))
# print(num + 10)


# # function with no parameters exercise 
# def hello_world_printer():
#     print("hello world")


# hello_world_printer()


# # function with one parameter exercise
# def name_printer(user_name):
#     print(user_name)


# name = input("Please enter your name.")
# name_printer(name)


# # Volume of a rectangular prism Programming Challenge
# length = int(input("Enter an integer that will represent the length of the Rectangle. "))
# width = int(input("Enter an integer that will represent the width of the rectangle. "))
# hight = int(input("Enter an integer that will represent the hight of the rectangle. "))


# def volume(length, width, hight):
#     return length * width * hight


# print("The volume of the rectangular prism is " + str(volume(length, width, hight)) + " cubic feet")


# #Celsius to Fahrenheit Solution with integers
# celsius = int(input("Please enter an integer that will represent celsius. "))


# def fahrenheit(cel):
#     return (1.8 * cel + 32)


# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

#Celsius to Fahrenheit Solution with round()
celsius = int(input("Please enter an integer that will represent celsius. "))


def fahrenheit(cel):
    return round(1.8 * cel + 32)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")