#Experiment 42
#Factorial of a number using for loop:
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter the required number : "))
Fct=1
for i in range(Nmb,0,-1):
    Fct = i*Fct
print("The factorial of the number",Nmb,"is",Fct)