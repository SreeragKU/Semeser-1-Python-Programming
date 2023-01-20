#Experiment 6:
#A program to enter the name of a student and marks of five subjects. Subsequently, also to calculate the total mark and percentage:

#Declaring a variable to which the user inputs the name of the student:
Nme= input("Enter the name of the student : ")

#Declaring another 5 variables to which the user inputs the mark of 5 different subjects:
Mks1= int(input("Enter the mark received in Python Programming (Max=100) : "))
Mks2= int(input("Enter the mark received in Digital Fundamentals (Max=100): "))
Mks3= int(input("Enter the mark received in Advanced Software Engineering (Max=100): "))
Mks4= int(input("Enter the mark received in Advanced Data Structures (Max=100): "))
Mks5= int(input("Enter the mark received in Web Programming (Max=100): "))

#Calculations:
Ttl= Mks1+Mks2+Mks3+Mks4+Mks5       #Total= Sum of all Marks
Prctg= 1/500*Ttl*100                   #Total Percentage = Sum of all marks / Total marks obtainable * 100

#Printing the result:
print("The name of the student is", Nme)
print("The total marks obtained = ",Ttl)
print("The total percentage obtained = ",Prctg,"%")