#Experiment 39:
#A program to count the occurrences of each word in a line of text:
#Declaring a variable to which the user inputs the required word:
Txt=input("Enter the required text : ")
Spt=Txt.split(" ")
Lst=list(Spt)
St=set(Spt)
for i in St:
    Ct=Lst.count(i)
    print("'",i,"' occurs",Ct,"times")