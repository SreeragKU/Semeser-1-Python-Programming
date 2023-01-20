#Experiment 32:
#A program to print pattern 2:
#Declaring a variable to which the user inputs the number of rows:
Rw=int(input("Enter the number of rows required : "))
i=Rw+1
while(i>=1):
    j=1
    while(j<i):
        print("*",end=" ")
        j=j+1
    print()
    i=i-1