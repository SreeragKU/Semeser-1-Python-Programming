#Experiment 14:
#A program to enter a string and swap the first and the last character of the string:
#Declaring a variable to which the user inputs the string:
Strg=input("Enter a string : ")
p1=Strg[0]
p2=Strg[-1]
p3=Strg[1:-1]
print("The first character : ",p1)
print("The last character : ",p2)
#Swapping the first and the last character of the string and printing the result:
print("The string after the first and last character is swapped : ",p2+p3+p1)

