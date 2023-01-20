#Experiment 22:
#A program to find the sum of even and odd numbers:
#Declaring a variable to which the limit is inputted by user:
Lt=int(input("Enter the limit value : "))
temp=1
SmE=0
SmO=0
#Using while loop to check every number until the value reaches temp=1:
while(temp<=Lt):
    if(temp%2==0):          #Eg, 4%2==0, which is even
        SmE=SmE+temp
    else:                   #Eg, 3%2!=0, hence is odd
        SmO=temp+SmO
    temp=temp+1
print("The sum of even numbers until",Lt,"is",SmE)
print("The sum of odd numbers until",Lt,"is",SmO)