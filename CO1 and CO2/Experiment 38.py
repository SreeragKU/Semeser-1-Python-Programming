#Experiment 38:
#A program to generate a list ordinal value of each element of a word using list comprehension:
#Declaring a variable to which the user inputs the required word:
Chr=input("Enter the required word : ")
Chr1=Chr.lower()
Lst=list(Chr1)
Lst1=[ord(i) for i in Lst]
print(Lst1)