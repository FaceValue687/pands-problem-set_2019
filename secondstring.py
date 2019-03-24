#Solution to problem #6
#This program takes a user input string and outputs every second word.
#Daria J. Ostrowska

#An input is requested and stored in a variable
#No need to provide for an exception input in case of numbers as numeric information will still be valid input
#as the input function by default converts all the information it receives into a string
text = input("Type something to test it out: ")
#I define words to go into the new sentence to contain every second word of the original sentence with 
#by using "text.split" + slicing command [::n]. The ".join()" method will concatenate the string. 
words = ' '.join(text.split( )[::2])
#Print output to the screen
print(words)

#Based on: https://www.geeksforgeeks.org/join-function-python/