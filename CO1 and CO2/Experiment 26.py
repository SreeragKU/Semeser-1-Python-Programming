#Experiment 43
#Generate Fibonacci series of N terms
#Declaring a variable to which user inputs the limit value.
Lt = int(input("Enter the limit number :"))
#The First two terms
n1=0
n2=1
count=0
if(Lt<=0):
   print("Please enter a positive integer")
elif(Lt==1):
   print("Fibonacci sequence upto",Lt,":")
   print(n1,end=" ")
else:
   print("Fibonacci sequence:")
   while(count<Lt):
       print(n1,end=" ")
       s = n1 + n2
       n1 = n2
       n2 = s
       count=count+1