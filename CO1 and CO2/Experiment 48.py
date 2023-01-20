#Experiment 49
#A program to display a pyramid of step numbers
#Declaring a variable to which the user inputs the number of rows
Rws=int(input("Enter the number of rows : "))
for i in range(1,Rws+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print(" ")
