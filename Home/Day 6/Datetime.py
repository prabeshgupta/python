#To work with date, import module datetime
import datetime

print(datetime.datetime.now().year)

"""
The datetime object has a method for formatting date into readable strings.

The method is called strftime(), and takes one parameter to specify the format of the returned string
"""

print(datetime.datetime.now().strftime("%A"))