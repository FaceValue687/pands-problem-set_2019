# Solution to problem 1.
# This program asks the user to input any positive integer and outputs the # sum of all numbers 
# between one and that number.

# The user should see "Your number" prompt on the screen. The value of the variable "x" is 
# "You number:" prompt here.
x = int(input ('Your number is: '))
# I say what happens if the user inputs "0", a negative integer or a floating-point number 
# I use the "If statement"
if x <= 0:
  print('Your number should only be a positive integer greater than 0')
else:
   ans = 0
   # use while loop to iterate un till zero
   while(x > 0):
       ans += x
       x -= 1
   print("The sum is", ans)
   # Operators '+=' and '-=' from
   # https://stackoverflow.com/questions/2632677/python-integer-incrementing-with

