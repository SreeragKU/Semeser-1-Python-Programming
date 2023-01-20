#Experiment 58
#A program to find the gcd of two numbers without using math function
Nmb1=int(input("Enter the first number : "))
Nmb2=int(input("Enter the second number : "))
gcd=0
if(Nmb1>Nmb2):
    i=1
    while(i<=Nmb2):
        if(Nmb1%i==0 and Nmb2%i==0):
            gcd=i
        i=i+1
else:
    i = 1
    while (i <= Nmb1):
        if (Nmb1 % i == 0 and Nmb2 % i == 0):
            gcd = i
        i=i+1
print("gcd of",Nmb1,"and",Nmb2,"is",gcd)
