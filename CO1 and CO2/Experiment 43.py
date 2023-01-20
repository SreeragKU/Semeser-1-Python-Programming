#Experiment 43
#A program to generate Fibonacci series using for loop
#Declaing a variable to which user inputs the limit
Lt=int(input("Enter the limit value until which Fibonacci series needs to be generated : "))
Nmb1=0
Nmb2=1
if Lt<=0:
    print("Please enter a positive number")
else:
    print(Nmb1,Nmb2,end=" ")
    for i in range(2,Lt):
        Nxt=Nmb1+Nmb2
        print(Nxt,end=" ")
        Nmb1=Nmb2
        Nmb2=Nxt