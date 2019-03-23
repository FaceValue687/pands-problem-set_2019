#Solution to problem #6
#This program takes a user input string and outputs every second word.
#Daria J. Ostrowska

#An input is requested and stored in a variable
#No need to provide for an exception input in case of numbers as numeric information will still be valid input
#as the input function by default converts all the information it receives into a string
text = input("Type something to test it out: ")
#The program calls on the split function to store each word of the user's sentence as a separate value
words = text.split(' ')
#I use the slicing command [::n] to make the program to go through the list of values from the beginning to 
#end in steps of 2 and printing the resulting output to the screen
print(words[::2])