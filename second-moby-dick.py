#A program that reads in a text file and outputs every second line, taking the file name from an argument
#on the command line.
#Daria J. Ostrowska

##A program that reads in a text file and outputs every second line, taking the file name from an argument
#on the command line.
#Daria J. Ostrowska

#I invite user input ("Tom_Jones_a_chapter.txt")
user_input = (input("Enter the name of the file : "))
#The program will open and read the user's input
with open(user_input, "r+") as work_file:
#and count lines starting from line #1
    for count, line in enumerate (work_file, start=1):
#if line number is not divisible by 2
        if count%2==0:
#it will print that line
            print(line)


#Adapted from: https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po?noredirect=1&lq=1


