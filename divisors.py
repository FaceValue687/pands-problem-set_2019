#Python Program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12

#I define the range of x so that only numbers between 1,000 and 10,000 (both numbers including)
for x in range (1000, 100001):

#I use the if statement to set the conditions for the execution of the program
#I use the modulus operandus % and the comparison operator == for the x's in range divisible by 6 and the modulus operandus % and the comparison 
#operator != for the x's in range not divisible by 12.
#I use the key word "and" to join the two conditions
    if x%6==0 and x%12!=0:

#I use the function print() to display the results on the screen
        print(x)

#Based on: http://www.openbookproject.net/thinkcs/python/english2e/ch04.html
     