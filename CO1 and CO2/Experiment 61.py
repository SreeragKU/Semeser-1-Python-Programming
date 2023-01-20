#Experiment 61
#Merge two dictionary
Dict1={}
Dict2={}
sz=int(input("Enter the size of first dictionary: "))
for i in range(sz):
    key=int(input("Enter the key element: "))
    value=int(input("Enter the value element: "))
    Dict1.update({key:value})
sz=int(input("Enter the size of second dictionary: "))
for i in range(sz):
    key=int(input("Enter the key element: "))
    value=int(input("Enter the value element: "))
    Dict2.update({key:value})
print("First dictionary is",Dict1)
print("Second dictionary is",Dict2)
Dict1.update(Dict2)
print("The merged dictionary is",Dict1)