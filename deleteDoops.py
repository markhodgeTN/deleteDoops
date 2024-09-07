import os

//Changes directories to where the files are located
folder = os.chdir("C:/Users/username/userfolder")

//Creates a list of all the files in the folders
files = os.listdir()

//Loops through the files. If "Copy" is in the file name, the file is deleted
for i in files:
    if "Copy" in str(i):
        os.remove(i)


//Let's the user know the program finished running
print("Finished")
