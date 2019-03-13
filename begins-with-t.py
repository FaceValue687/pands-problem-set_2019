#Solution to problem 2
#This program outputs whether or not today is a day that begins 
#with the letter T

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yes, today begins with T")
elif datetime.datetime.today().weekday() == 3:
  print("Yes, today begins with T")
else:
  print("No, today doesn't begin with T")
  



