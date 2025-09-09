# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops

#  Loop Functions - Perform Repetitive Tasks when the Condition is True
#  Loops let you execute certain code or actions repetitively while the condition remains true and terminate when they are false.
#  Loops use while and for statements
#  One defining characteristic of loop functions is the incrementing or decrimenting of a counter to eventually break the loop.
print("Defining x, the initial variable:")
x = 0

# Define a while loop
print("\nwhile loop example:")
while (x < 5):          # while Condition - starting the loop
    print(x)            # Action performed while the condition is true
    x = x + 1           # Increment to eventually break the loop

print("\nwhile loop with input example:")
answer = input("May I continue? (y to continue): ")
while (answer == "y"):                          # while Condition - starting the loop
    print("Thank you!")                         # Action performed while the condition is true
    answer = input("May I continue? (y to continue): ")   # Re-prompt to eventually break the loop 
# *** While loops are better suited for situations where the number of iterations is not known.
# *** Remember, a while loop that is never false will create infinite iterations.

# Define a for loop
print("\nfor loop example:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for d in days:          # for Condition to iterate over the provided list
    print(d)            # Action performed for each item in the collection
# *** For loops are better suited for iterating over a collection of items where the number is known.
# *** The loop will automatically terminate when the end of the collection is reached.
# *** Remember, just like while loops, for loops that are never false create infinite iterations.

# Use the break and continue statements
print("\nfor loop with break example:")
for d in days:
    if (d == "Wed"):    # if Condition to check for a specific item
        print("It's Wednesday, my dudes. AAAAAAAAAHHHH!")  # Action performed if the condition is true
        break           # break statement to exit the loop
    print(d)            # Action performed for each item in the collection until the break statement is encountered

print("\nfor loop with continue example:")
for d in days:
    if (d == "Fri"):    # if Condition to check for a specific item
        continue        # continue statement to skip the current iteration
    print(d)            # Action performed for each item in the collection except when the continue statement is encountered

# Using the enumerate() function to get an index and an item
print("\nfor loop with enumerate() example:")
for i, d in enumerate(days):   # enumerate() function to get both the index of the collection and the item
    print(i, d)                # Action performed for each item in the collection with its index
