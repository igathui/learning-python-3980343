# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
print(myint)    # This is an integer
print(myfloat)  # This is a floating point number
print(mystr)    # This is a string
print(mybool)   # This is a boolean

# Operators are used to perform operations on variables
print(myint + myfloat)  # Addition operator
print(myfloat - myint)  # Subtraction operator
print(myint * 2)        # Multiplication operator
print(myfloat / 2)      # Division operator
print(myint % 3)        # Modulus operator
print(myint ** 2)       # Exponentiation operator
print(myint // 3)       # Floor division operator
print(-myint)           # Negation operator
# And many more...

# NB: The addition and multiplication operators can also be used for string manipulation
anotherstr = " - This is another string"
repeatstr = "Wow! "
print(mystr + anotherstr)   # String concatenation
print(repeatstr * 3)        # String replication
# *** You cannot add or multiply strings with most other data types

# Logical and comparison operators that return boolean values
print(myint > 5)      # Greater than
print(myint < 5)      # Less than
print(myint >= 5)     # Greater than or equal to
print(myint <= 5)     # Less than or equal to
print(myint == 5)     # Equal to
print(myint != 5)     # Not equal to
print(myint > 5 and myfloat < 20)   # Logical AND
print(myint > 5 or myfloat < 20)    # Logical OR
print(not(myint > 5))               # Logical NOT
# Logical XOR is not a built-in operator, but can be implemented using !=

# re-declaring a variable works
myint = "abc" # This is now a string
print(myint)