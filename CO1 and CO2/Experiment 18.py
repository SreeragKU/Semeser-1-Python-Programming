#Experiment 18
#A program to input integer n and compute n+(n*n)+(n*n*n)
#Declaring a variable to which the user inputs the required number:
Intn=int(input("Enter the value of n : "))
#Splitting the equation into three and declaring two variables for the second and third parts:
Intn1=Intn*Intn
Intn2=Intn*Intn*Intn
#Printing the sum
print("n+(n*n)+(n*n*n) =",Intn+Intn1+Intn2)
