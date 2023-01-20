#Experiment 27:
#A program to check whether numbers between a range is Armstrong or not:
#Declaring two variable to which the user inputs the required range
Lt1=int(input("Enter the lower limit of range : "))
Lt2=int(input("Enter the upper limit of range : "))
Sm=0
temp1=Lt1
while(temp1<Lt2+1):
        while(temp1 > 0):
                Rem = temp1 % 10
                Cb = Rem ** 3  # Exponentiation (**) to find cube of digits
                Sm = Sm + Cb
                temp1 = temp1 // 10  # Floor division to receive the largest possible integer
        if(Lt1==Sm):
                print("The number",Lt1,"is an Armstrong number")
        else:
                print("The number",Lt1,"is not an Armstrong number")
        Lt1=Lt1+1
        temp1=Lt1
        Sm=0

