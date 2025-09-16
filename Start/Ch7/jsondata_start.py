# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# JSON FUNCTIONS - Using Python to Work with JSON, a Popular Internet Format
# JSON stands for JavaScript Object Notation

print("Using the 'Useless Facts' API as sample JSON data:")
# Open the URL and read the data
weburl = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Status: ", weburl.getcode())
# Read the JSON data from the source
print("\nLoading the raw JSON data:")
data = weburl.read()
print(data)

# Print the content of the 'text' field
print("\nConverting the raw JSON into a Python dictionary:")
theJson = json.loads(data)
print(theJson)

print("\nPrinting out the random fact:")
print(theJson["text"])