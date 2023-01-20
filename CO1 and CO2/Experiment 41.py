Str=input("Enter the required string : ")
Chr=Str[0]
Chr1=Str[0].lower()
Str=Str.replace(Chr,'$')
Str=Str.replace(Chr1,'$')
Str1=Chr+Str[1:]
print("The required string : ",Str1)
Str=input("Enter the required word ending with either 'ing' or 'ly' : ")
if(Str[-3:]=="ing"):
    Str=Str+"ly"
    print(“The required word: “,Str)
else:
    Str=Str+"ing"
    print(“The required word: “,Str)
