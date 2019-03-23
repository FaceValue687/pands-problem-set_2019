#Solution to problem #1.
#This program asks the user to input any positive integer and outputs the sum of all numbers 
#between one and that number.

#The user should see "Please enter a positive integer" prompt on the screen. The value of the variable "x" is 
#a number the user chose to enter.
x = int(input ('Please enter a positive integer: '))
#I say what happens if the user inputs "0" or a negative integer by using the the "If statement"
if x <= 0:
#If the above is true the following prints to the screen:
  print('Your number should only be a positive integer greater than 0')
#If x<0 I initialise the answer to zero. I indicate by using "ans" that it will be used in new calculations. 
else:
   ans = 0
#I use the while loop to check the condition of input x being>0:
   while(x > 0):
#while the above true my answer is the input number plus that input number decreased by 1, plus the decreased 
#number futher decreased by 1, until x=0, e.g. 3+(3-2)+(2-1)=6, i.e the new x is decreased by 1 until x=0. 
      ans += x
      x -= 1
   print("The sum is", ans)

#Based on: 1. https://stackoverflow.com/questions/2632677/python-integer-incrementing-with
#and:      2. https://python-textbok.readthedocs.io/en/1.0/Loop_Control_Statements.html 

