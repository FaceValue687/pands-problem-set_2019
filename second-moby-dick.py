#A program that reads in a text file and outputs every second line, taking the file name from an argument
#on the command line.
#Daria J. Ostrowska

#
text_file=open("Tom_Jones_a_chapter.txt","r")
with open("Tom_Jones_a_chapter.txt", "r+") as work_file:
    for count, line in enumerate (work_file, start=1):
        if count%2==0:
            print(line)


#Adapted from: https://stackoverflow.com/questions/30551945/how-do-i-get-python-to-read-only-every-other-line-from-a-file-that-contains-a-po?noredirect=1&lq=1


