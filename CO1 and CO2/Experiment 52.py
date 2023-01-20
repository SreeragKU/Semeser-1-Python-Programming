#Experiment 52
#A program to accept a list of words and return length of longest word.
#Declaring a list to which user inputs the words
Lst=[]
temp=0
choice=True
while(choice==True):
    e = input("Enter the words to be added to the list : ")
    Lst.append(e)
    choice = input("Enter Stop to end the List. Press enter to continue : ")
    if(choice=="Stop"):
        choice=True
        break;
    else:
        choice=True
print("The Entered list is :",Lst)
le=len(Lst)
for i in range(le):
    if(len(Lst[i])>len(Lst[-1-i])):
        temp=Lst[i]
    else:
        temp=Lst[-1-i]
print("The longest word in the list is",temp)

