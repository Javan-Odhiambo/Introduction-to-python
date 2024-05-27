# Functions
#  - Functions are a way to group code together

# Function definition
def name_of_function(parameters):
    ...

# Function call
# name_of_function(arguments)

# Example:
# No parameters
def print_hello():
    print("Hello")

# print_hello()
# print_hello()

# One Parameter
def say_hello(name):
    print(f"Hello {name}")

# say_hello("Jane")

# Multiple Parameters
def add_two_values(a, b):
    print(a + b)

# add_two_values(1, 2)

# Default Parameters
def add_with_default(a, b=0):
    print(a + b)

# add_with_default(1) # -> 1
# add_with_default(1, 2) # -> 3
# add_with_default(1, b=6) # -> 7


# endless parameters
def add_endless_values(*args, **kwargs): # args -> tuple, kwargs -> dictionary
    sum = 0
    for number in args:
        sum += number # sum = sum + number
    print(sum)


add_endless_values(1, 2, 3, 4, 5, 10, 20)

# Return value
def add(a, b):
    sum = a + b
    return sum 

result = add(1, 2)

