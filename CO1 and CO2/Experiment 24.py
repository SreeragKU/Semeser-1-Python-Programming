#Experiment 24:
#A program to find the sum of the digits:
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter the required number : "))
temp=Nmb
Sm=0
#Using while loop to check whether the inputted number is greater than zero
while(temp>0):
    rem=temp%10         #Remainder will be the last digit of the inputted number.
    Sm=rem+Sm
    temp=temp//10       #Floor divison to receive the closest integer
print("The sum of digits of the number",Nmb,"is",Sm)