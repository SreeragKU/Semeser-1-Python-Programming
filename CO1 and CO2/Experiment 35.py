#Experiment 35:
#A program to generate positive list of numbers from a given list of integers using list comprehension:
#Declaring a variable to which the user inputs the size of the list:
Lst=[]
Lst1=[]
Lst2=[]
s=int(input("Enter the size of the list : "))
#Using loop to enter the elements into the list:
for i in range(s):
    e=int(input("Enter any integers to be added to the list : "))
    Lst.append(e)
print("The entered list is : ",Lst)
#List comprehension
Lst1=[i for i in Lst if i>0]
Lst2=[i for i in Lst if i<0]
print("The list of positive numbers is", Lst1)
print("The elements removed from the list are", Lst2)
