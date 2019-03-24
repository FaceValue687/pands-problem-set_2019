#Solution to problem #8
#This program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15".
#Daria J. Ostrowska

#I use the "import" statement to import the out-of-the-box Python datetime object - this will allow me to work 
#with methods for date and time values.
import datetime
#I use the "datetime.datetime.today" class method to create an instance of datetime object for today's date 
today=datetime.datetime.today()
#I use the "strtime" to set the required format for the time and date using a pre-defined library of character
#strings for every component, e.g. "%A" to return the full name of the weekday.
print(today.strftime("%A, %B %d %Y at %H:%M"))


#Based on: https://pymotw.com/3/datetime/, and:
#          http://strftime.org/