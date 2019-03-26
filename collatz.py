#Solution to problem #4
#This program asks the user to input any positive integer and outputs the successive values of the following
#calculations: at each step the next value is calculated by taking the current value and, if it is even, 
#it is divided by two, but if it is odd, it is multiplied by three and 1 is added. The program ends if 
#the current value is one.
#Daria J. Ostrowska


num = int(input("Please enter a positive integer: "))
while num!=1:
    if num%2 == 0:
        num = num/2
    else:
        num = (num*3)+1
    print((num)