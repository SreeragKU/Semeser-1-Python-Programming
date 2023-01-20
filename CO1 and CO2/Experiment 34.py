#Experiment 34:
#A program to display future leap years from current year to a final year entered by user:
#Declaring a variable to which the user inputs the limit year:
LLt=int(input("Enter the limit year until which leap years must be checked: "))
for i in range(2022,LLt+1):
    if(i%4==0):
        print("The year",i,"is a leap year")