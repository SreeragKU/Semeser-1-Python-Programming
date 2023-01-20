#Experiment 51
#A program to check whether a number is palindrome or not using for loop
#Declaring a variable to which user inputs the required number
Nmb=input("Enter the required number : ")
for i in range(len(Nmb)):
    if(Nmb[i]!=Nmb[-1-i]):
        print("The number",Nmb,"is not a palindrome")
        break;
else:
    print("The number",Nmb,"is a palindrome")