#Experiment 36
#A program to generate the square of N numbers using list comprehension:
#Declaring a variable to which the user inputs the limit value:
Lt=int(input("Enter the limit value until which the square of numbers need to be generated: "))
Lst=[]
Lst=[i*i for i in range (Lt+1)]
print("The list of squares of numbers until the inputted number : ",Lst)