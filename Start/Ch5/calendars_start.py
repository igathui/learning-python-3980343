#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar
from itertools import count

# CALENDAR - Working with dates and times using the Calendar module
# Operations on dates and times using the Calendar module are done in plain text or HTML format.
# Create a plain text calendar
print("Create a plain text calendar:")  
c = calendar.TextCalendar(calendar.MONDAY)
c_string = c.formatmonth(2026, 1) 
print(c_string) 

# Create an HTML formatted calendar
print("\nCreate an HTML formatted calendar:")
hc = calendar.HTMLCalendar(calendar.MONDAY)
hc_string = hc.formatmonth(2026, 1)
print(hc_string)

# Loop over the days of a month
# Zeroes mean that the day of the week is in an overlapping month
print("\nLoop over the days of a month:")
for i in c.itermonthdays(2026, 8):
    print(i)


# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
print("\nPrinting out the names of the months and days:")
for mo in calendar.month_name:
    print(mo)

for day in calendar.day_name:
    print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("\nCalculate days based on a rule:")

print("Team meetings will be on the first Friday of every month. \nThose dates are:")
for m in range(1, 13):
    cal = calendar.monthcalendar(2026, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print(f"{meetday} {calendar.month_name[m]}")
