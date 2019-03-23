#Solution to problem #7
#Python Program that takes a positive floating point number as input and outputs an approximation 
#of its square root.
#Daria J. Ostrowska

#I invite input from the user
x=float(input("Enter a positive number: "))
#I define tolerance for recursive calls, i.e. how close I want the final approximation of the square root
#to be to the actual #square root of "x", where the tolerance is the difference between the value of "x"
# and the square root of a given approximation 
tolerance=0.000001
#I set the initial guess of the square root of "x" to "1" so the "while True" loop can compute at least 
#one estimate
estimate=1.0
#To perform successive approximations I use the "while True: " loop
while True:
#Successive better estimates are obtained
    estimate=(estimate+x/estimate)/2
#abs function to obtain an absolute value of the estimate as it can be positive of negative
    difference=abs(x-estimate**2)
#for as long as "difference" is <= "tolerance"
    if difference<=tolerance:
#I use "break" to stop the loop from executing at the approximation that corresponds to difference<=tolerance,
#i.e. when the difference between the square root of the estimate and "x" becomes <= tolerance value
        break
#I use the function "print" to display the best approximation of the square root of "x" given the size 
#of the tolerance and the set estimate
print("The approximation of the square root of your number is: ", estimate)

#Based on: Lambert, K.A. (2011). Fundamentals of Python. First Programs. Boston, Massachusetts, USA:
#Course Technology 

