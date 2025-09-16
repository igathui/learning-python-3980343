#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

# READING FILES - Read files using the built-in Python file methods
print("Opening the sample.txt in read mode")
samplefile = open("sample.txt", "r")                            # Open the file for reading
if samplefile.mode == "r":                                      # Check if the file is in read mode
    # Executes if the file is in any other mode
    contents = samplefile.read()                                # Read the entire file
    print(contents)                                             # Print the contents of the file
else:
    # Executes if the file is in read mode
    print("The file is not in read mode!")
samplefile.close()                                              # Close the file when done   

# Open the file and read the contents
samplefile = open("sample.txt", "r")
if samplefile.mode == "r":
    # Use the read() function to read the entire file
    filelines = samplefile.readlines()
    for line in filelines:
        print(line)
else:
    print("The file is not in read mode!")
samplefile.close()