#Experiment 28:
#A program to compare and print the colors in one list that are not contained in the second:
#Declaring two variable to which the user inputs the required colors:
Lst1=input("Enter the colors in List 1 separated by commas: ")
Lst2=input("Enter the colors in List 2 separated by commas: ")
#Splitting elements into individual strings:
Spt1=Lst1.split(",")
Spt2=Lst2.split(",")
#Converting them to two different sets:
St1=set(Spt1)
St2=set(Spt2)
#Finding the difference between the two sets:
St3=St1-St2
#Converting the result back to a list:
Lst3=list(St3)
print(Lst3)