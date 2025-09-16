# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet

import urllib.request

# RETRIEVEING INTERNET DATA - Using Python to retreive internet data

print("Using urllib.request to retrieve status code")
weburl = urllib.request.urlopen("https://example.com")
print("Result code: ", weburl.getcode())

print("\nReading website data from request:")
data = weburl.read()
print(data)