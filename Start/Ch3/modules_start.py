# LinkedIn Learning Python course by Joe Marini
# Working with modules of code

# Modules - Libraries from the Python Standard Library and Beyond
# Go to https://docs.python.org/3/tutorial/modules.html for more information
# Very similar to the node_modules concept in Node.js

# Import the math module, which contains features for working with mathematics
import math

print("The square root of 144 is:", math.sqrt(144))


# Import a specific part of the module so you can refer to it more easily
from math import log1p

print("The natural log of 2.71828 is:", log1p(2.71828))


# Import a module and give it a different name
import random as r

print("A random number between 1 and 10:", r.randint(1,100))

# In addition to functions, some modules contain useful constants
from math import pi, e

print("The value of pi is:", pi)
print("The value of e is:", e)

# Generate a random number between 100 and 200
num = r.randint(100, 200)

# Try some of the math functions for yourself here:
print("The square root of", num, "is:", math.sqrt(num))
print("The natural log of", num, "is:", log1p(num))

# Use the 3rd party tabulate module to print tabulated data:
from tabulate import tabulate # import the tabulate module

# Sample data
data = [
  ["Product", "Price", "Stock"],
  ["Laptop", 999.99, 45],
  ["Mouse", 24.99, 128],
  ["Keyboard", 59.99, 89]
]

# Create a formatted table
print("\n Using the tabulate module to print a formatted table:")
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))