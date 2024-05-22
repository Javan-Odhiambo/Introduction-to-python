# Basic syntax
# Variables
firstName = "John"
first_name = "John"
FirstName = "John"
FIRST_NAME = "John"

# Data types
# Strings (str)
string = "Hello World!"
string_2 = 'Hello World!2'

# Integers (int)
interger = 60

# Floats (float)
floating_point_number = 60.0

# Booleans  (bool)
true = True
false = False

# Input and output
# name = input("Enter your name: ")
# print("Hello", name)

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
# print("Full Name: " + full_name)

# Mathematical operators
# Addition => +
# print("Addition of 5 + 6 = ", 5 + 6)

# Subtraction => -
# print("Subtraction of 15 - 6 = ", 15 - 6)

# Multiplication => *
# print("Multiplication of 5 * 6 = ", 5 * 6)

# Division => /
# print("Divison of 25 / 6 = ", 25 / 6)

# Modulus => %
# Returns the remainder of the division
# print("Modulus of 15 % 6 = ", 15 % 6)

# Exponentiation => **
# Returns the power of a number
# print("Exponentiation of 2 ** 2 = ", 2 ** 2)

# Floor division => //
# Returns the quotient of the division
# print("Floor division of 15 // 6 = ", 15 // 6)

# Type conversion
# Read on Truthy and Falsy values

# float()
# bool()
# str()
# int()

# Logical operators
# and
# print(1 > 0 and 2 > 1) # True
# print(1 > 0 and 2 < 1) # False

# or
# print(1 > 0 or 2 > 1) # True
# print(1 < 0 or 2 > 1) # True
# print(1 < 0 or 2 < 1) # False

# not
# print(not 1 > 0) # False
# print(not 1 < 0) # True

# Comparison operators
# == (Equal to)
# != (Not equal to)
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)


# Control Flow
# number = input("Enter a number: ")
# print("The type of the variable number is: ", type(number))
# number = float(number)

# If statements
# if number > 0:
#     print("The number is positive")


# If else statements
# -2, -1, 0, 1, 2
# if number > 0:
#     print("The number is positive")
# else:
#     print("The number is negative")

# If elif else statements
# if number > 0:
#     print("The number is positive")
# elif number == 0:
#     print("The number is zero")
# else:
#     print("The number is negative")

# Loops 

# Range function
# range(stop)
# range(5) => 0, 1, 2, 3, 4

# range(start, stop)
# range(1, 5) => 1, 2, 3, 4

# range(start, stop, step)
# range(1, 10, 2) => 1, 3, 5, 7, 9

# For loops
# for value in range(10):
#     print(value)

# for char in "Introduction to Python":
#     print(char)

# While loops
# Runs until a condition is False

count = 0
# while count < 10:
#     print(count)
#     count = count + 1

# Break and Continue statements

# Break statement -> Exits the loop
# while count < 10:
    # if count == 5:
    #     break
    # print(count)
    # count = count + 1

# Continue statement -> Skips the current iteration
# while count < 10:
#     count = count + 1
#     if count == 5:
#         continue
#     print(count)

# Infinite loop -> A loop that never ends
# Occurs when the condition is always True
# THIS IS BAD!!!
# To stop the loop, press Ctrl + C
# while count < 10:
#     if count == 5:
#         continue
#     print(count)
#     count = count + 1

# Functions

