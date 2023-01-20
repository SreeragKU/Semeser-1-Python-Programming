#Experimen 60
#Sort dictionary in ascending and descending order
Dict={}
Lst=[]
sz=int(input("Enter the size of the dictionary: "))
for i in range(sz):
    key=eval(input("Enter the key element: "))
    value=eval(input("Enter the value element: "))
    Dict.update({key:value})
Lst=list(Dict.items())
Lst.sort()
Dict=dict(Lst)
print("Ascending order is",Dict)
Lst=list(Dict.items())
Lst.sort(reverse=True)
Dict=dict(Lst)
print("Descending order is",Dict)