#Experiment 48
#A program to get a string from an input string where all occurrences of first character replaced with ‘$’, except first character
#Declaring a variable to which the user inputs the required string
Str=input("Enter the required string : ")
Chr=Str[0]
Chr1=Str[0].lower()
Str=Str.replace(Chr,'$')
Str=Str.replace(Chr1,'$')
Str1=Chr+Str[1:]
print(Str1)