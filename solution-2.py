#Solution to problem 2
#This program outputs whether or not today is a day that begins 
#with the letter T
import datetime
if datetime.datetime.today().weekday() == 'T':
   print('Yes - today begins with a T.')
else:
   print('No, today does not begin with a T.')
# Based on the video "Run a Python program" of 18/01/2019