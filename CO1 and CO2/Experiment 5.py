#Experiment 5:
#Swapping two variables:

#Declaring a variable to which the user inputs the first value:
Vbl1=input("Enter the value of the first variable : ")

#Declaring another variable to which the user inputs the second value:
Vbl2=input("Enter the value of the second variable : ")

#Printing the initial values of variables:
print("The initial values are : ")
print("Variable 1 =", Vbl1)
print("Variable 2 =", Vbl2)

#Swapping the values:
Vbl1,Vbl2=Vbl2,Vbl1

#Printing the result:
print("The values after swapping are : ")
print("Variable 1 =", Vbl1)
print("Variable 2 =", Vbl2)