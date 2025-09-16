# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini


from datetime import date
from datetime import datetime

# DATE OBJECTS
# Get today's date from the simple today() method from the date class
print("Using the date class:")
today = date.today()
print(f"Today's date is {today}")

# Print out the date's individual components
print("\nPrinting out individual components of the date class:")
print(f"Date components: {today.day} {today.month} {today.year}")

# Retrieve today's weekday (0=Monday, 6=Sunday)
print("\nPrinting out today's weekday:")
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print(f"Today's weekday is #{today.weekday()}, which is a {days[today.weekday()]}")

# DATETIME OBJECTS
# Get today's date from the datetime class
print("\nGetting today's date from the datetime class:")
today = datetime.now()
print(f"Today's date and time is {today}")

# Get the current time
print("\nGetting the current time:")
t = datetime.time(datetime.now())
print(f"The current time is {t}")