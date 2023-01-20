#Experiment 12:
#A program to check whether a number is positive or negative number:
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter any number : "))
#Using if, elif and else function to check whether the number is equal to or less than zero or greater than zero:
if(Nmb==0):
    print("The number(",Nmb,") is zero")
elif(Nmb<0):
    print("The number (",Nmb,") is a negative number")
else:
    print("The number (",Nmb,") is a positive number")