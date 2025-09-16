
#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#

from datetime import datetime

# DATE FORMATTING - Formatting time and date output
# Times and dates can be formatted using a set of predefined string control codes
# Usually denoted by % (e.g. %Y, %m, %d)
print("This is the datetime object without formatting")
now = datetime.now()
print(now)


#### Date Formatting ####
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print("\nDate formatting:")
print(now.strftime("The current year is: %Y"))              # Full year with century
print(now.strftime("%a, %d, %B, %Y"))                       # Abbreviated day, day of month, full month, full year
print(now.strftime("%A, %d, %b, %y"))                       # Full day, day of month, abbreviated month, abbreviated year

# %c - locale's date and time, %x - locale's date, %X - locale's time
print("\nLocale datetime formatting:")
print(now.strftime("Locale date and time: %c"))             # The locale is my current system's location datetime details
print(now.strftime("Locale date: %x"))                      # Date display format
print(now.strftime("Locale date: %X"))                      # Time display format

#### Time Formatting ####
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print("\nTime formatting:")
print(now.strftime("Current time: %I:%M:%S %p"))            # 12-Hour:Minute:Second:AM
print(now.strftime("24-hour time: %H:%M"))                  # 24-Hour:Minute

