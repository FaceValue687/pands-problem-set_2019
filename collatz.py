#Solution to problem #4
#This program asks the user to input any positive integer and outputs the successive values of the following
#calculations: at each step the next value is calculated by taking the current value and, if it is even, 
#it is divided by two, but if it is odd, it is multiplied by three and 1 is added. The program ends if 
#the current value is one.
#Daria J. Ostrowska

#I set up a "while True" loop to repeat a section of code that takes the user input in case of wrong input
#User input must be>1 as the Collatz conjecture defines a sequence of positive integers that starts with any 
#number>1.
while True:
   try:
    	number = int(input("Please enter a positive integer bigger than 1: "))
#I use the "assert" condition to be able to raise an exception if the above condition is not met
    	assert(number>1)
#and if the condition is true I set the program to continue from there 
    	break
#If the condition is not true, exception is raised
   except:
       print("Number entered must be bigger than")
 
while number!=1:
    if number%2 == 0:
        number = number/2
    else:
        number = (number*3)+1
    print(number)


#Based on: https://www.cis.upenn.edu/~matuszek/cit590-2016/Lectures/15%20Functional%20Python.pdf
#      and:https://www.quora.com/What-does-while-true-do-in-python  