#Experiment 21
#A program to check whether a number is Armstrong or not:
#Declaring a variable to which the user inputs the required number:
ArmSt = int(input("Enter a number: "))
Sm = 0
temp=ArmSt
#Finding the sum of the cube of each digit:
while temp > 0:
   Rem = temp % 10
   Cb = Rem ** 3          #Exponentiation (**) to find cube of digits
   Sm=Sm+Cb
   temp=temp// 10        #Floor division to receive the largest possible integer
#Using if, else function to check whether a number is Armstrong or not:
if(ArmSt==Sm):
   print("The number",ArmSt,"is an Armstrong number")
else:
   print("The number",ArmSt,"is not an Armstrong number")