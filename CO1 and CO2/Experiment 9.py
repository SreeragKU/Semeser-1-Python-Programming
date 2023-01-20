#Experiment 9:
#A program to generate a simple calculator

#Declaring two variables to which the user inputs the numbers to be operated upon:
Nmb1= int(input("Enter the first number : "))
Nmb2= int(input("Enter the second number : "))

#Declaring another variable to which the user can input the desired operation:
Optn= int(input("1= Sum, 2= Difference, 3= Quotient, 4=Product : "))

#Checking the operation through if elif conditional statements and printing the results:
if Optn == 1:
    Rslt= Nmb1+Nmb2
    print("Sum of",Nmb1,"and",Nmb2,"is",Rslt)
elif Optn == 2:
    Rslt= Nmb1-Nmb2
    print("Difference between",Nmb1,"and",Nmb2,"is", Rslt)
elif Optn == 3:
    Rslt= Nmb1/Nmb2
    print("Quotient of",Nmb1,"by",Nmb2,"is",Rslt)
elif Optn == 4:
    Rslt= Nmb1*Nmb2
    print("Product of",Nmb1,"and",Nmb2,"is",Rslt)
else:
    print("Not a valid operation")