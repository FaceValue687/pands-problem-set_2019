#A program that asks the user to input a positive integer and tells the user whether or not the 
#number is a prime
#Daria J. Ostrowska
# taking input from user
number = int(input("Please enter a positive integer: "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")

#Source: https://beginnersbook.com/2018/01/python-program-check-prime-or-not/