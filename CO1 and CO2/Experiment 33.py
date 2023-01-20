#Experiment 33:
#A program to print pattern 3:
#Declaring a variable to which the user inputs the number of rows:
Rw=int(input("Enter the number of ascending rows required : "))
i=1
while(i<=Rw):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
i=Rw
while(i>=1):
    j=1
    while(j<i):
        print("*",end=" ")
        j=j+1
    print()
    i=i-1