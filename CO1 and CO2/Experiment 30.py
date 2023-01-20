#Experiment 30:
#A program to print a list after removing all even numbers from it:
#Declaring a variable to which the user inputs the size of list:
Lst=[]
Lst1=[]
Lst2=[]
s=int(input("Enter the number of elements in the list : "))
for i in range (s):
    e=int(input("Enter the elements in the list : "))
    Lst.append(e)
    if(e%2!=0):
        Lst1.append(e)
    else:
        Lst2.append(e)
print("The elements in the list are", Lst)
print("The required list is",Lst1)
print("The elements removed from the list are", Lst2)

