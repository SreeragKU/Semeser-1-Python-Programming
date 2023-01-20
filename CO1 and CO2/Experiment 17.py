#Experiment 17:
#A program to input 3 colours with comma and display the first and last colours
#Declaring a variable to which the user inputs the colours separated by comma:
Clrs=input("Enter three colours with commas to separate each : ")
#Splitting the colours into three strings:
Clspt=Clrs.split(",")
#Printing the first and the last colour:
print("The first colour is",Clspt[0])
print("The last colour is",Clspt[-1])