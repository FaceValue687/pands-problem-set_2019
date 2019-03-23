#Solution to problem #5
#A program that asks the user to input a positive integer and tells the user whether or not the 
#number is a prime
#Daria J. Ostrowska

##The user should see "Please enter a positive integer greater than 1" prompt on the screen. The value of the 
#variable "x" is the number the user chose to enter
x = int(input ('Please enter a positive integer greater than 1: '))

#prime number is always greater than 1, so we set the first condition in the "if" statement
if x >1:
#We set a range for "i" which will be our divisor for "x"
    for i in range(2, x):
#If our division of "x" by "i" - i" being either "2" or "x", doesn't give a reminder
        if (x %i) == 0:
#it is not a prime number, so
            print(x, "is not a prime number")
            break
    else:
#Note: "2" prints "is a prime number" as well as it is included as the start of the range, and the range can
#only be defined incrementally, so the next value of "x" in the range is "3" not "2".
        print(x, "is a prime number")
#If the entered number is less than or equal to 1 then it is not prime number
else:
   print(x, "is not a prime number")

#Source: https://beginnersbook.com/2018/01/python-program-check-prime-or-not/