#Solution to problem #3
#Python Program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12
#Daria J. Ostrowska

#I define the range of x so that only numbers between 1,000 and 10,000 (both numbers including) are taken 
#into account
for x in range (1000, 100001):

#I use the if statement to set the conditions for the execution of the program
#I use the modulus operandus % and the comparison operator == for the x's in range divisible by 6 and the
#modulus operandus % and the comparison operator != for the x's in range not divisible by 12
#The modulus operandus operation checks whether there is any reminders for the divsion operations by 6 or 12
#and the operators "==" and "!=" check for the boolean True and False conditions
#I use the key word "and" to join the two conditions
    if x%6==0 and x%12!=0:
#I use the function print() to display the results on the screen
        print(x)

#Based on: http://www.openbookproject.net/thinkcs/python/english2e/ch04.html
     