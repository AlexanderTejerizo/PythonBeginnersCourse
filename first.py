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

# #Celsius to Fahrenheit Solution with round()
# celsius = int(input("Please enter an integer that will represent celsius. "))


# def fahrenheit(cel):
#     return round(1.8 * cel + 32)


# print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")


# # Miles Per Gallon Programming Challenge

# from random import randint
# # generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
# fuel = randint(10, 25)
# # generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
# miles = randint(200, 400)
# # calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
# print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# # displays the number of gallons of fuel that the car's fuel tank can hold
# print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# # displays the number of miles that the car can travel on a full tank
# print("The car can travel " + str(miles) + " miles on a full tank.")


# # Grading Programming Challange
# grade = int(input("What is the Student's grade? \fEnter: "))

# if grade >= 90:
#     letter = "A"
# else:
#     if grade >= 80:
#         letter = "B"
#     else: 
#         if grade >= 70:
#             letter = "C"
#         else: 
#             if grade >= 60:
#                 letter = "D"
#             else:
#                 letter = "F"

# print("The studetnt's grade is " + letter + ".")


# #Roman Numeral Programming Challange
# from random import randint
# ran_num = randint(1,10)

# if ran_num == 1:
#     print("I")
# elif ran_num == 2:
#     print("II")
# elif ran_num == 3:
#     print("III")
# elif ran_num == 4:
#     print("IV")
# elif ran_num == 5:
#     print("V")
# elif ran_num == 6:
#     print("VI")
# elif ran_num == 7:
#     print("VII")
# elif ran_num == 8:
#     print("VIII")
# elif ran_num == 9:
#     print("IX")
# elif ran_num == 10:
#     print("X")


# # While loop Exercise 1
# counter = 10

# while counter > 0:
#     print(counter)
#     counter -= 1


# # # Programming Challenge: Sum of Numbers From A Positive Integer
# # pos_int is a variable which holds a user entered integer.
# pos_int = int(input("Please enter a positive integer."))
# # This variable stores the initial value of pos_int before it is used in the loop so
# # that later it can be used to display pos_int's initial value in the output.
# int_init = pos_int
# # This is a variable which will be used to hold the sum of all the integers from pos_int.
# summed = 0
# # The while loop will run while pos_int's stored integer value is greater than 0
# while pos_int > 0:
#     # This is the equivalent of summed = summed + pos_int
#     # In other words: new value of summed = old value of summed + new value of pos_int
#     summed += pos_int
#     # This will decrement pos_int so that pos_int will eventually equal 0 and the while
#     # loop will stop running its code.
#     pos_int -= 1
 
# print(int_init)  # displays the initial value of pos_int
# print(summed)    # displays the sum of integers from pos_int


# # For loop exerscise 1
# word = "Hello World"

# for Letters in word:
#     print(Letters)


# # Programming Challenge: Find The Number of Characters in A String
# string1 = input("Type a sentance. ")
# count = 0

# for letter in string1:
#     count += 1

# print("There are " + str(count) + " characters in " + string1 + ".")


# #Programming Challenge: Fizz Buzz

# for integers in range(1, 51):
#     if integers % 3 and integers % 5 == 0:
#         print("FizzBuzz")
#     elif integers % 3 == 0:
#         print("Fizz")
#     elif integers % 5 == 0:
#         print("Buzz")
#     else:
#         print(integers)


# # Programming Challenge: Factorial
# pos_int = int(input("Please type a positive integer, its factorial will be displayed below."))
# init_pos_int = pos_int

# for i in range(pos_int, 1, -1):
#     pos_int *= i

# print("The factorial of " + str(init_pos_int) + " is " + str(pos_int) + ".")


# # string methods 1 exercises
# mixed_case = "A Song of Ice and Fire"

# print(mixed_case.isupper())
# print(mixed_case.islower())
# print(mixed_case.upper())
# print(mixed_case.lower())
# print(mixed_case.istitle())

# title_case = mixed_case.title()

# print(title_case)

# mixed_case.startswith("A")
# print(mixed_case.startswith("A"))

# mixed_case.endswith("e")
# print(mixed_case.endswith("e"))

# words = mixed_case.split()
# print(words)
# print(" ".join(words))
# print("".join(words).isalpha())


# # string methods 2 exercises
# the_string = "North Dakota"
# center_plus = the_string.center(16, "+")

# print(the_string.rjust(17))
# print(the_string.ljust(17, "*"))
# print(center_plus)
# print(the_string.lstrip("North "))
# print(center_plus.rstrip("+"))
# print(center_plus.strip("+"))
# print(the_string.replace("North", "South"))


# # Programming Challenge: String Reverser
# user_string = input("Please enter a string.")
# reversed = ""
 
# for item in range(len(user_string) -1, -1, -1):
#     reversed += user_string[item]
 
# print(reversed)
# print(user_string[4])


# # Programming Challenge: Word Counter
# str_1 = "James Bond is 007.".split()
# str_2 = "When the moon hits your eye like a big pizza pie, that's amore!".split()
# str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
# saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
# shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
# shrimp burger, shrimp sandwich. That- that's about it.".split()

# def word_count(string):
#     number = 0
#     for i in string:
#         number = number + 1
#     return number


# print(word_count(str_1))
# print(word_count(str_2))
# print(word_count(str_3))

# str_1 = "James Bond is 007."
# str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
# str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
# saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
# shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
# shrimp burger, shrimp sandwich. That- that's about it."
 
 
# # This function reduces the string to letters, numbers, spaces, hyphens, and apostrophes, and assigns that string to
# # the variable spaces_and_letters so that the number of words in it can by found by counting spaces between words.
# def word_counter(words):
#     spaces_and_letters = ""
#     word_count = 1
#     for i in words:
#         if i.isalnum() or i.isspace() or i == "-" or i == "'":
#             spaces_and_letters += i
#     for j in spaces_and_letters:
#         if j == " ":
#             word_count += 1
#     return word_count
 
 
# print(word_counter(str_1))
# # print(word_counter(str_2))
# # print(word_counter(str_3))


# # introduction to lists exercises
# list_one = [1, 2.1, False, "Hello", [4,5,6]]
# list_two = list("Hello")

# print("e" in list_two)
# print("a" not in list_two)


# # indexes and list slicing exercises
# list_one = [[0,2], [4,6], [8,10], [12,14]]
# list_two = ["chair", "table", "desk", "lamp", "bed"]
# list_three = [0.98, 8.76, 6.54, 4.32]

# print(list_one[0])
# print(list_one[3][1])
# print(list_two[-5])
# print("Most people own atleast" + " " + str(list_one[0][1]) + " " + list_two[0] + "s.")
# print(list_three[1:])
# print(list_three[1:3])
# print(list_three[:2])


# # del and list methods exercises
# arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# del(arctic_animals[4])
# arctic_animals.remove("elephant")
# arctic_animals.append("arctic fox")
# arctic_animals.insert(2, "snowy owl")
# arctic_animals.sort()
# print(arctic_animals)
# print(arctic_animals.index("reindeer"))
# print(arctic_animals.pop())

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
arctic_animals.remove("elephant")
arctic_animals.append("arctic fox")
arctic_animals.insert(2, "snowy owl")  
arctic_animals.sort()  
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())