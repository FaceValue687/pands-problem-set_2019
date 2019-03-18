#Python Program that takes a positive floating point number as input and outputs an approximation 
#of its square root.

#I need the program to take input from the user in the form of a positive number: I set #a variable "num" to 
#do that. I use the input() function as the argument for the float() method for the variable's legal values. 
#Because I use the float()method I don't need to specify to the user that only a postive FLOATING number is 
#allowed, but I want to make to remind the user that no negative values are allowed. 

#float() method ensures a variable is a floating point number
#I set the "while True:" loop"and "try-except" block to handle the illegal values

while True:
	try:
		num = float(input("Enter a positive number: "))
#I use the "assert" statement to evaluate if the accompanying expression is true
		assert(num > 0), "Number must be bigger than 0"
#If "assert" is true the "while True" loop breaks; if not true it runs again until true
		break
#I name the exception for the user in the "except clause"
	except:
		print("This is a negative number")
#I use the built-in function math.sqrt() which for a given float gives the same value as the last best-estimate
#recursive call in the newtons_method (Source: https://stackoverflow.com/questions/9595135/how-do-i-calculate-square-root-in-python).
import math
print("An approximation of the square root of your number is", math.sqrt(num))