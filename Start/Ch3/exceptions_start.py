# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions


# Exception Handling - Catch and Handle Errors in Code 
# Go to https://docs.python.org/3/library/exceptions.html for the extensive list

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
from typing import final


print("Trying to divide by zero:")
# x = 10/0                    # This will raise a ZeroDivisionError
# print(x)


# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
print("\nUsing try/except to catch the error:")
try:
    x = 10/0
except:
    print("Well that didn't work!")
    
# You can also catch specific exceptions
print("\nUsing try/except to catch specific exceptions:")
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
except ValueError as e:
    print("You did not provide a valid number!")
    print(e)
finally:
    print("Finally always runs!")