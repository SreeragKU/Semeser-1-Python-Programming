#Experiment 15
#A program to enter three numbers and find the largest among them
#Declaring three variable to which the user inputs the required numbers:
Nmb1=int(input("Enter the first number : "))
Nmb2=int(input("Enter the second number : "))
Nmb3=int(input("Enter the third number : "))
#Using 'max' function to find the largest of the three numbers:
Nmb4=max(Nmb1,Nmb2,Nmb3)
print("The largest among the numbers(",Nmb1,",",Nmb2,",",Nmb3,") is",Nmb4)