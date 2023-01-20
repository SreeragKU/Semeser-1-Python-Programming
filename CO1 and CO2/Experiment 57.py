#Experiment 57
#A program to check whether a number is Armstrong or not
Nmb1=int(input("Enter a number : "))
temp=Nmb1
rev=0
for i in range(temp,0,-1):
    rem=temp%10
    rev=rev+(rem**3)
    temp=temp//10
if(rev==Nmb1):
    print("The number",Nmb1,"is an Armstrong number")
else:
    print("The number",Nmb1,"is not an Armstrong number")
