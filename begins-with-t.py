#Solution to problem 2
#This program outputs whether or not today is a day that begins #with the letter T
#Daria J. Ostrowska

import datetime
# I define the date object and the time object and use the "combine" function to build my datetime.
# This circumvents the persisent error "datetime.datetime has not attribute datetime" that I get with
# all the other methods 
# (hours, minutes)
start_time = datetime.time(1, 0)
# (year, month, day)
start_date = datetime.date(2019, 3, 17)
# Create a datetime object
start_datetime = datetime.datetime.combine(start_date, start_time)
# Gets the day of the week for a given date.
# Returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
weekday_number = start_datetime.date().weekday()
if weekday_number==1:
   print("Today begins with T")
elif weekday_number==3:
   print("Today begins with T")
else:
   print("Today does not begin with T")

#Based on: https://brohrer.github.io/datetime_tricks.html
#Note: "Because of the naming convention, calls to datetime can be confusing. Datetime is the name of the package,
#a module within the package, and the object. So when we combine our date and time, we call it with 
#the apparently redundant datetime.datetime prefix. The first datetime references the package, the second 
#datetime references the module, and combine() is a function within that module."
#Source: Paragraph "Wrangling dates and times in python" at: https://brohrer.github.io/datetime_tricks.html 
  



