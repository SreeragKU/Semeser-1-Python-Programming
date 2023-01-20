#Experiment 25:
#A program to check whether a number is prime number or not:
#Declaring a variable to which the user inputs the required number:
Nmb=int(input("Enter the required number : "))
j=0
i=2
while(i<=Nmb//2):
    if(Nmb%i==0):
        j=j+1
        break
    i=i+1
if(j==0 and Nmb!=1):
    print(Nmb,"is a Prime number")
else:
    print(Nmb,"is not a prime number")
