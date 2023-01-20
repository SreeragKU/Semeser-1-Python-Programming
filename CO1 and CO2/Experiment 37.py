#Experiment 37:
#A program to form a list of vowels selected from a given word using list comprehension:
#Declaring a variable to which the user inputs the required word:
Chr=input("Enter the required word : ")
Chr1=Chr.lower()
Lst=list(Chr1)
Lst1=[]
Lst1=[i for i in Lst if i=='a' or i=='e' or i=='i' or i=='o' or i=='u']
print(Lst1)