# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions

# Functions - A Block of Reusable Code
# Functions are named blocks of code that are designed to perform specific tasks within certain parameters.
# They typically take an input, process it, and return an output.
# Functions help to make code more modular, easier to read, and easier to maintain.
# Functions are defined using the 'def' keyword, followed by the function name and parentheses.
# The code block within every function starts with a colon (:) and is indented.

# Define a basic function
print("Simple function example: ")

def hello_func():                               # Function definition
    print("hello world!")                       # Function body
    name = input("What is your name? ")
    print("Nice to meet you,", name)

hello_func()                                    # Function call. You can call this function as many times as needed without rewriting the code.
# *** This function does not take any parameters or return a value.

# Function that takes parameters
print("\nFunction with parameters example: ")
def hello_func2(greeting):                      # Function definition with parameters
    print("hello world!")                       # Function body
    name = input("What is your name? ")
    print(greeting, name)

hello_func2("What's up")                        # Function call with argument passed to the parameter
# *** This function does not return a value.


# Function that returns a value
print("\nFunction that returns a value example: ")
def cube_func(x):                               # Function definition with parameter
    return x * x * x                            # Function body with return value

result = cube_func(3)                           # Function call with return value assigned to a variable
print(result)                                   # Print the result

# Function with default value for an parameter
print("\nFunction with default parameter value example: ")
def hello_func3(greeting="Hi, ", name=None):    # Function definition with default parameter values
    print("hello world!")                       # Function body
    if name == None:
        name = input("What is your name? ")
    print(greeting, name)

hello_func3()                                   # Function call with no arguments, uses default values
hello_func3("Joe", "Salutations, ")             # Function call overriding default values
# *** Remember to override default parameters from left to right only or the function will not work as intended.

# Function with variable number of parameters
print("\nFunction with variable number of parameters example: ")
def multi_add(start, *args):                           # Function definition with variable number of parameters
    result = start                                  # Initialize result variable 
    for x in args:                              # Iterate through the variable parameters
        result = result + x                     # Add each parameter to the result
    return result                               # Return the result

print(multi_add(1,2,3))                         # Function call with multiple arguments
print(multi_add(4,5,6,7,8,9,10))                # Function call with more arguments
# *** The *args parameter allows the function to accept any number of positional arguments