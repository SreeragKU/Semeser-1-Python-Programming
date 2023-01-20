#Experiment 44
#A program to enter two list of integers and check whether the lists are of same length.
#Declaring two lists in which user inputs the required integers
Lst1=[]
Lst2=[]
choice=True
while(choice==True):
    e = int(input("Enter the elements of the first list : "))
    Lst1.append(e)
    choice =input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        choice=True
        break;
    else:
        choice=True
while(choice==True):
    e = int(input("Enter the elements of the second list : "))
    Lst2.append(e)
    choice =input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        break;
    else:
        choice=True
if len(Lst1)==len(Lst2):
    print("\nBoth list are of equal sizes and has",len(Lst1),"elements")
else:
    print("\nThe two lists are not of equal length since",len(Lst1),"is not equal to",len(Lst2))






