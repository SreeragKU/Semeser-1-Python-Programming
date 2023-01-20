#Experiment 39:
#A program to prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead:
#Declaring a variable to which the user inputs the size of the list:
Lst=[]
Lst1=[]
s=int(input("Enter the size of the list : "))
#Using loop to enter the elements into the list:
for i in range(s):
    e=int(input("Enter any integers to be added to the list : "))
    Lst.append(e)
    if(e<=100):
        Lst1.append(e)
    else:
        e="over"
        Lst1.append(e)
print("The entered list is : ",Lst)
print("The required list is :",Lst1)