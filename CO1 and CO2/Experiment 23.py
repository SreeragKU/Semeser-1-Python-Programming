#Experiment 23:
#A program to reverse of a number:
#Declaring a variable to which user inputs the number:
Nmb=int(input("Enter a number, reverse of which will be displayed below: "))
rev=0
#Using while loop to check whether the inputted number is greater than zero
while(Nmb>0):
    rem=Nmb%10              #Remainder will be the last digit of the inputted number.
    rev=rev*10+rem
    Nmb=Nmb//10             #Floor divison to receive the closest integer
print("Reverse of the number is", rev)