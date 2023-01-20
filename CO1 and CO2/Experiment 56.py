#Experiment 56
#A program to find the factors of a number using for loop
Nmb=int(input("Enter a number : "))
Lst=[]
for i in range(1,Nmb+1):
    if(Nmb%i==0):
        Lst.append(i)
print("The factors of",Nmb,"are",Lst)
