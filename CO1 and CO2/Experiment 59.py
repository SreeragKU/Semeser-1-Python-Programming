#Experiment 59
#A program to generate a list of 4 digit numbers which are even and have perfect squares
Lwlmt=int(input("Enter the lower limit : "))
Uplmt=int(input("Enter the upper limit : "))
Lst=[]
for i in range(Lwlmt,Uplmt):
    if(i%2==0):
        for j in range(1,i):
            if(j*j==i):
                Lst.append(i)
print(Lst)
if(len(Lst)==0):
    print(" ")
