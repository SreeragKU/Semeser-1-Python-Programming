#Experiment 20:
#A program  to check whether a number is palindrome or not:
#Declaring a variable to which the user inputs the required number:
Palndr= int(input("Enter the required number : "))
Temp=Palndr
rev=0
#Using while loop to reverse the inputted number:
while(Temp>0):
    rem=Temp%10             #Remainder will be the last digit of the inputted number
    rev=rev*10+rem
    Temp=Temp//10           #Floor divison to receive the closest integer
#Using if and else functions to check whether the number is palindrome or not:
if(Palndr==rev):
    print("The number",Palndr,"is a palindrome")
else:
    print("The number",Palndr,"is not a palindrome")