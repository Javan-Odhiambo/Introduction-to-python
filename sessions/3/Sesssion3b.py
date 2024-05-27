# List comprehension # ASSIGNMENT
# Look up set data type in Python
# GO LEARN ABOUT THE MATH MODULE IN PYTHON

# Dynamically typed language -> Python, JavaScript, Ruby, PHP
# Statically typed language -> Java, C++, C#, Swift, Kotlin


# Lists, Tuples, and Dictionaries
# list -> A collection of elements that are ordered and changeable. Allows duplicate members.
# list is defined by square brackets
names = ["Javan", "Tom", "Newton", "Judy"]
empty_list = []

numbers = [1, 2, "3", 4, "5", True, 4.5]

# Accessing and maninpulating 
# Accessing elements in a list
# indexing starts from 0
# ["Javan", "Tom", "Newton", "Judy"] -> 0, 1, 2, 3
# ["Javan", "Tom", "Newton", "Judy"] -> -4, -3, -2, -1


# print(names[0]) # -> Javan
# print(names[1]) # -> Tom
# print(names[7]) # -> IndexError: list index out of range

# print(names)
# names[0] = "Javan Otieno"
# print(names)

# looping through a list
# for i in range(len(names)):
#     print(names[i])

print("************")
# element in this case is a variable representing a single name in the list
# for element in names:
#     print(element) 

# Slicing
# list[start:stop:step]
# names[1:3] # -> ["Tom", "Newton"]
# names[2:] # -> ["Newton", "Judy"]
# names[:2] # -> ["Javan", "Tom"]

# list methods
# append() -> Adds an element at the end of the list
# print(names)
names.append("Merlin Eve")
# print(names)

# pop() -> Removes the last element from the list
# print(names)
last_name = names.pop()
# print(names)
# print(last_name)

# Tuples -> A collection of elements that are ordered and unchangeable. Allows duplicate members.
# tuple is defined by round brackets
names_tuple = ("Javan", "Tom", "Newton", "Judy", "Judy")
# print(type(names_tuple))

# Accessing elements in a tuple
# print(names_tuple[3]) # -> Judy
# names_tuple[0] = "Javan Otieno" # -> TypeError: 'tuple' object does not support item assignment


# Dictionaries -> A collection of elements that are unordered, changeable, and indexed. No duplicate members.
# Consists of key -> value pairs
Benson = {
        "first_name": "Benson",
        "age": 25,
        "is_student": True,
        "courses": ["Python", "JavaScript", "React"]
    }

# Accessing elements in a dictionary
# print(Benson["first_name"]) # -> Benson

Benson["age"] = 29
# print(Benson)

# Dictionary methods
# get() -> Returns the value of the specified key
# print(Benson.get("first_name")) # -> Benson

# update() -> Updates the dictionary with the specified key-value pairs
Benson.update({"followers": 3000})
# print(Benson)

# print(Benson.keys())
# print(Benson.values())
# print(Benson.items())

# Looping through a dictionary
# for key in Benson:
#     print(key, Benson[key])

# for key, value in Benson.items():
#     print(key, value)
    
# for value in Benson.values():
#     print(value)


# Working with strings
# String methods
programming_language = "      Python       "
# upper() -> Converts a string into uppercase
# print(programming_language.upper())
# lower() -> Converts a string into lowercase
# print(programming_language.lower())
# strip() -> Removes any whitespace(space, tab, new line) from the beginning or the end
# print(programming_language.strip())
# count() -> Returns the number of times a specified value occurs in a string
# print(programming_language.count("o")) # -> 2

# replace() -> Replaces a string with another string
# split() -> Splits the string into substrings if it finds instances of the separator
# join() -> Joins the elements of an iterable to the end of the string
# format() -> Formats specified values in a string
# find() -> Searches the string for a specified value and returns the position of where it was found

# READ MORE ON STRINGS

# Introduction to modules and importing modules
# Modules -> A file containing a set of functions you want to include in your application

# OPTION 1
# import mathematics
# print(mathematics.add(5, 8))
# print(mathematics.subtract(5, 8))
# print(mathematics.multiply(5, 8))

# OPTION 2
# from mathematics import add
# print(add(5, 8))

# OPTION 3
# imports all functions from the mathematics module
# SHOULD BE AVOIDED
# from mathematics import * 
# print(multiply(5, 8))

# OPTION 4
# from mathematics import add as addition
# print(addition(5, 8))

