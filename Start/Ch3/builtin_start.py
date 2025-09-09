# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions

# Built-In Functions - Default Functions of the Python Language
# Go to https://docs.python.org/3/library/functions.html for the extensive list
print("Example string and list:")
mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]
print(mystring)
print(mynumbers)

# The len() function calculates the length of a sequence
print("\nLength of the string and list:")
print(len(mystring))                # Indicates the number of characters in the string
print(len(mynumbers))               # Indicates the number of items in the list

# The max() and min() functions will find the largest and smallest value in a sequence
print("\nMax and min of string the list:")
print(max(mystring))                # Indicates the largest character in the string
print(min(mystring))                # Indicates the smallest character in the string
print(max(mynumbers))               # Indicates the largest number in the list
print(min(mynumbers))               # Indicates the smallest number in the list

# The str() function will return a string version of an object
print("\nString prefix and number:")
prefix = "result: "
result = 5
print(prefix + str(result))         # Concatenating the string and number using str() 
# *** Remember that you cannot concatenate strings and other data types directly. Use str() to convert numbers to strings first

# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
print("\nRange of numbers:")
for i in range(5,15):
    print(i)

for j in range(0,len(mystring),2):
    print(mystring[j])


# The print() function itself is pretty flexible - you can embed variables directly in it
print("\nEmbedded variables:")
greeting = "Hello!"
count = 10
print(f"{greeting} You have {count} new messages.")     # Print out interpolated string
# *** Note the f before the string to enable embedded variables.

# There are plenty more built-in functions - explore the docs to see what else is available!