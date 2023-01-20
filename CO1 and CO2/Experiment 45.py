#Experiment 45
#A program to enter two list of integers and check whether the list sums to same value.
#Declaring two lists in which user inputs the required integers
Lst1=[]
Lst2=[]
choice=True
sum1=0
sum2=0
while(choice==True):
    e = int(input("Enter the elements of the first list : "))
    sum1=sum1+e
    Lst1.append(e)
    choice =input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        choice=True
        break;
    else:
        choice=True
while(choice==True):
    e = int(input("Enter the elements of the second list : "))
    sum2=sum2+e
    Lst2.append(e)
    choice =input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        break;
    else:
        choice=True
print("The inputted lists are :")
print(Lst1,"\n",Lst2)
print("Sum of integers of List 1 is : ",sum1)
print("Sum of integers of List 2 is : ",sum2)
if(sum1==sum2):
    print("\nThe sum of values of both list are equal")
else:
    print("\nThe sum of values of both lists are not equal")
