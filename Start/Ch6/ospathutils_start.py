#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path

# OPERATING SYSTEM PATH UTILITIES - Working with the os.path module
# Print the name of the OS
print("Print the name of the OS:")
print(os.name)

# Check for item existence and type
print("\nCheck file existence and type:")
if path.exists("sample.txt"):
    print("The file exists!")
    print(path.isfile("sample.txt"))
    print(path.isdir("sample.txt"))
else:
    print("The file does not exist!")

# Work with file paths
print("\nWorking with file paths:")
print("The file's path: ", path.realpath("sample.txt"))
print("The file's path and name: ", path.split(path.realpath("sample.txt")))

# Get the file time metadata
import time 
from datetime import datetime

print("\nFinding the file's time metadata:")
# Using the time module
tc = time.ctime(path.getctime("sample.txt"))
tm = time.ctime(path.getmtime("sample.txt"))
print(tc)
print(tm)
# Using the datetime module
print(datetime.fromtimestamp(path.getctime("sample.txt")))
print(datetime.fromtimestamp(path.getmtime("sample.txt")))

# Calculate how long ago the item was modified
print("\nCalculate the time since the file was modified:")
td = datetime.now() - datetime.fromtimestamp(path.getmtime("sample.txt"))
print(f"It has been {td} since the file was modified.")
print(f"or {td.total_seconds()} seconds.")