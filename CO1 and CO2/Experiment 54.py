#Experiment 54
#A program to count the number of characters (character frequency) in a string.
#Declaring a variable to which user inputs the required string
Str=input("Enter the required string : ")
Lst=list(Str)
St=set(Str)
count=0
for i in St:
    for j in range(0,len(Lst)):
        if(i==Lst[j]):
            count=count+1
    print(i,"occurs",count,"times")
    count=0

