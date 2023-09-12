
# Task 1
# Using the variable called current_datetime, subtract 15 days from the current time.
# Hint: use .strftime() method to reformat the time
# If today is 8/07/2021, your result should look like this: 2021-06-23

import datetime as dt
current_date = dt.date(day = 8, month = 7, year = 2021)
new_date = current_date - dt.timedelta(days = 15)
print(new_date)

# Task 2
# Using the variable called current_datetime, add 7 days to your current day.
# Your result should look like this, if today is 8/07/2021: 2021-07-15

import datetime as dt
current_date = dt.date(day = 8, month = 7, year = 2021)
new_date = current_date + dt.timedelta(days = 7)
print(new_date)

# Task 3
# Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.
# Steps:
# Start by creating a datetime of the current date, January 1st, 2020: current_date = datetime(year=2020, month=1, day=1)
# Do your calculations to add 25 days to current_date. Create a string and print it out. Your result should look like this:
# Hello Friedrich, your rent of 300 € is due on 26 January, 2020.

import datetime as dt
current_date = dt.datetime(year = 2020, month = 1, day = 1)
date_1 = current_date.strftime("%B %d, %Y")
print("Current date is:", date_1)
due_date = current_date + dt.timedelta(days = 25)
date_2 = due_date.strftime("%d %B, %Y")
print("Due date is:", date_2)
print("Hello Friedrich, your rent of 300 € is due on 26 January, 2020.")

