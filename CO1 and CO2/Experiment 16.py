#Experiment 16:
#A program to input the filename with extension and print only the extension:
#Declaring a variable to which the user inputs the filename with extension:
FlNme=input("Enter the filename with extension(Eg: image.jpg) : ")
#Using split function to separate the string into two:
Spt=FlNme.split(".")
#Printing the second string after splitting:
print("The extension of the file is",Spt[-1])