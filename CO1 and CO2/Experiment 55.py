#Experiment 55
#A program to find the reverse of a number using for loop.
#Declaring a variable to which user inputs the required number
Nmb=int(input("Enter the required number : "))
rev=0
Lst=[]
for i in str(Nmb):
    x=int(i)
    Lst.append(x)
l=len(Lst)
for k in range(-1,-l-1,-1):
    rev=rev*10+Lst[k]
print("Reverse of",Nmb,"is",rev)
