# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: A One-Dimensional Ordered Collection of Items
# Sequences are lists, tuples, sets (...and strings). 
# They may contain values of different data types (except strings).
print("Types of sequences:")
mylist = [0, 1, 2.125, "Three", False, 5]       # A list
mytuple = (6, 7, 8.725, "Nine", True, 11)       # A tuple
myset = {12, 13, 14.325, "Fifteen", False, 17}  # A set
mystr = "This is a string"                      # A string
# *** Lists and sets are mutable, tuples and strings are immutable.
# *** Lists, tuples, and strings are ordered/indexed, sets are unordered.
# *** Sets do not allow duplicate values.

# You can get the length of a sequence using the "len()" function:
print("\nLengths of sequences:")
print(len(mylist))  # The "len()" function returns the length of a list,
print(len(mytuple)) # or a tuple,
print(len(myset))   # or a set,
print(len(mystr))   # or a string.

# To access a member of a sequence type, use []. Negative indices count from the end of the sequence:
print("\nAccessing elements of sequences:")
print(mylist[3])    # This is the 4th element of the list (indices begin at 0)
print(mytuple[0])   # This is the 1st element of the tuple
print(mystr[5])     # This is the 6th character of the string
print(mylist[-1])   # This is the last element of the list
print(mytuple[-2])  # This is the second to last element of the tuple
print(mystr[-3])    # This is the third to last character of the string
# *** Remember that sets are unordered, so you cannot access elements by index.

# Add a list to another list
print("\nCombining lists:")
anotherlist = [6, 7, 8]
print(mylist + anotherlist)  # This is list concatenation
print(anotherlist * 3)       # This is list replication
# *** Just like strings, lists can be concatenated and replicated.

# Use slices to get parts of a sequence
print("\nSlicing sequences:")
print(mylist[1:4])      # This is a slice of the list from index 1 to 3 (non-inclusive of 4)
print(mytuple[2:5:2])     # This is a slice of the tuple from index 2 to 4, stepping by 2
print(mystr[0:10:3])     # This is a slice of the string from index 0 to 9, stepping by 3
# *** Remember that sets are unordered, so you cannot slice them.

# You can use slices to reverse a sequence
print("\nReversing sequences:")
print(mylist[::-1])      # This is the list reversed
print(mytuple[::-1])     # This is the tuple reversed
print(mystr[::-1])       # This is the string reversed
# *** Remember that sets are unordered, so you cannot reverse them.  
