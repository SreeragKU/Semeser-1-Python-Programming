#Experiment 49
#A program to generate a list of four-digit numbers in a given range with all their digits even and the number is a perfect square.
#Declaring a variable to which user inputs the range of 4-digit numbers
import math
LwLt=int(input("Enter the lower limit four digit number : "))
UpLt=int(input("Enter the upper limit four digit number : "))
k=0
for i in range(LwLt,UpLt):
    rt=math.sqrt(i)
    rti=int(math.sqrt(i))
    if(rt==rti):
        if(i%2==0):
            for k in str(i):
                x=int(k)
                if(x%2==0):
                    temp=i
                else:
                    temp=0
                    break;
            if(temp!=0):
                print(i,"is a four digit number with a perfect square and all its digits being even")












