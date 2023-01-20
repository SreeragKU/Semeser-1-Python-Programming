#Experiment 53
#A program to find the sum of all elements in a list
#Declaring a list to which user inputs the words
Lst=[]
sum=0
choice=True
while(choice==True):
    e = int(input("Enter the integer to be added to the list : "))
    Lst.append(e)
    choice = input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        choice=True
        break;
    else:
        choice=True
for i in range(len(Lst)):
    sum=sum+Lst[i]
print("The sum of all elements in the list is",sum)