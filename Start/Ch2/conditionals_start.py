# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements

# Conditionals Functions - Perform a Task when Condiction is True
# Conditional statements let you execute certain code or actions when the condition is true.
# Conditional flow uses if, elif, else
print("Defining x and y:")
x, y = 100, 100
print (x, y)

# if, elif and else
print("\nPerform the conditional flow:")
if x < y:                           # if Condition - starting conditional flow
    print("x is less than y")       
elif x == y:                        # else if Condition (optional) - additional condition if the first is false
    print("x is equal to y")    
else:                               # else Condition (also optional) - default action if all conditions are false
    print("x is greater than y");

# Conditional statements let you use "a if C else b"
print("\nUsing a conditional statments in a single line:")
result = "x is less than y" if (x < y) else "x is greater than or equal to y"
print(result)
# *** This is a shorthand way of writing simple if-else statements in a single line.