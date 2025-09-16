#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import datetime
from datetime import timedelta
from time import strftime

# TIMEDELTA - Operating on dates and times 

# A timedelta is a duration of time represented in days, seconds, and microseconds
# Construct a basic timedelta and print it
print("Constructing a basic timedelta:")
print(timedelta(days=365, hours=5, minutes=12))

# Print today's date
print("\nUsing today's date...")
now = datetime.now()
print(f"Today's date and time is {now}")

# Print today's date one year from now
print("\nCreating a timedelta of one year:")
print(f"In one year, it will be {now + timedelta(days=365)}")

# Create a timedelta that uses more than one argument
print("\nCreating a timedelta that uses more than one argument:")
print(f"In two weeks and 3 days, it will be {now + timedelta(weeks=2, days=3)}")


# Calculate the date 1 week ago, formatted as a string
print("\nCreating a timedelta that goes back in time:")
t = datetime.now() - timedelta(weeks=1)
s = strftime("%A, %d %B %Y")
print(f"One week ago it was {s}")


### How many days until April Fools' Day?
print("\nCalculating the timedelta between two dates:")
today = date.today()                                    # Today's date
afd = date(today.year, 4, 1)                            # April Fools' Day

if afd < today:
    print(f"April Fools' Day has already passed by {(today-afd).days} ago.")
    afd = afd.replace(year=today.year + 1)

time_to_afd = afd - today
print(f"It is just {time_to_afd.days} until April Fools' Day!")