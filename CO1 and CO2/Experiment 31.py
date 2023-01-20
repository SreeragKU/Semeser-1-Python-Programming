#Experiment 31:
#A program to print pattern 1:
#Declaring a variable to which the user inputs the number of rows:
Rw=int(input("Enter the number of rows required : "))
i=1
while(i<=Rw):
    j=1
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1