#Experiment 19:
#A program to find the factorial of a number using while loop:
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter the required number : "))
Fct=1
temp=Nmb
#Using while loop to check whether the inputted number is less than or equal to 1:
while(1<=Nmb):
    Fct=Nmb*Fct
    Nmb=Nmb-1
print("The factorial of the number",temp,"is",Fct)