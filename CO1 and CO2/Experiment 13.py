#Experiment 13:
# A program to input 2 strings and swapping the first character of both strings:
#Declaring two variable to which the user inputs the two strings:
Strg1=input("Enter the first string : ")
Strg2=input("Enter the second string : ")
#Printing the two strings together:
Strg3=Strg1+" "+Strg2
print("The entered string is",Strg3)
#Swapping the position of the first character of both strings:
p1=Strg1[0]
p2=Strg1[1:]
p3=Strg2[0]
p4=Strg2[1:]
print("The string after swapping the character at the first position : ",p3+p2+" "+p1+p4)