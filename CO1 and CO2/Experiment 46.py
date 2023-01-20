#Experiment 46
#A program to enter two list of integers and check whether any value occurs in both.
#Declaring two lists in which user inputs the required integers
Lst1=[]
Lst2=[]
choice=True
count=0
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
temp1=Lst1[0]
for i in range(0,len(Lst1)):
    for j in range(0,len(Lst2)):
        if(Lst1[i]==Lst2[j]):
            temp=Lst1[i]
            count=count+1
    if(i==0):
        print(temp,"occurs in both lists and occurs",count,"times in list 2")
    elif(temp1!=temp):
        print(temp, "occurs in both lists and occurs", count, "times in list 2")
    count=0
    temp1=temp