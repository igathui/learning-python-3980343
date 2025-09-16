# LinkedIn Learning Python course by Joe Marini
# Write files using the built-in Python file methods

# WRITING FILES - Manipulate files using the built-in Python file methods
# Open a file for writing and create it if it doesn't exist
print("Open a file for writing and create it if it doesn't exist:")
samplefile = open("sample.txt", "w+")                          # Open for writing and create if it doesn't exist
samplefile.write("This is a sample file.\n")                   # Write some text to the file
samplefile.write("This is another line of text.\n")      
samplefile.close()                                             # Close the file when done

# Open a file for reading
print("\nOpening the file for reading:")
samplefile = open("sample.txt", "r")                           # Open for reading
for line in samplefile:                                        # Loop over the lines of the file
    print(line)                                                # Print the lines
samplefile.close()                                             # Close the file when done

# Open the file for appending text to the end
print("\nAppending the text to the end of the file:")
samplefile = open("sample.txt", "a+")                          # Open for appending
samplefile.write("This is a is an addendum to the file.\n")    # Write some text to append to the file
samplefile.write("This is another line of text.\n")      
samplefile.write("Woah! Another line of text.\n") 
samplefile.close()                                             # Close the file when done

# write some lines of data to the file


# close the file when done
