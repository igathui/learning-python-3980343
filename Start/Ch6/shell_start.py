#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from zipfile import ZipFile

# FILESYSTEM SHELL METHODS - Working with the os.path module

# Make a duplicate of an existing file
print("Creating a copy of a file:")
if path.exists("newsample.txt"):
    # # Get the path to the file in the current directory
    src = path.realpath("newsample.txt")
    # ## Let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"
    # ## Now use the shell to make a copy of the file
    # shutil.copy(src, dst)  # ** This will not change the original file's metadata
    # ## Rename the original file
    # os.rename("sample.txt", "newsample.txt")
    
    # Mow put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)
    # More fine-grained control over ZIP files
   

    # with ZipFile("testzip.zip", "w") as newzip:
    #     newzip.write("newsample.txt")
    #     newzip.write("sample.txt.bak")