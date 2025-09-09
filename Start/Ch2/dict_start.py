# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionaries: A Two-Dimensional Unordered Collection of Pairs
# Dictionaries are collections of key:value pairs, where each key has a corresponding value.
# Like sequences, dictionaries may contain values of different data types for both keys and values.
# However, unlike most sequences, dictionaries are unordered and the keys must be unique and immutable
print("An example dictionary:")
mydict = {
    "one" : 1,
    "two" : 2,
    3 : "three",
    4.5 : ["four","point","five"],
    False : {False, False, True}
}
print(mydict)

# Dictionaries are accessed via keys
print("\nAccessing dictionary elements:")
print(mydict["one"])    # Accessing the value for key "one"
print(mydict[3])        # Accessing the value for key 3
print(mydict[False])    # Accessing the value for key False

# You can also set dictionary data by creating a new key
print("\nSetting new dictionary elements:")
mydict["five"] = 5
mydict[6] = (6, "six")
print(mydict)

# Trying to access a nonexistent key will produce an error
print("\nTrying to access a nonexistent key:")
# print(mydict["seven"])  # This will raise a KeyError

# To avoid this, you can use the "in" operator to see if a key exists
print("\nChecking for existence of keys:")
print("one" in mydict)      # should return True
print("seven" in mydict)    # should return False

# You can retrieve all of the keys and values from a dictionary
print("\nRetrieving keys and values:")
print(mydict.keys())    # Returns a view of all the keys in the dictionary
print(mydict.values())  # Returns a view of all the values in the dictionary


# You can also iterate over all the items in a dictionary
print("\nIterating over key:value pairs:")
for key, val in mydict.items():
    print(key, val);