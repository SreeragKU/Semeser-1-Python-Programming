import numpy as n
a1 = n.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
a2 = a1.reshape(6, 2)
print("Reshaped array:\n",a2)

x = n.arange(30)
array = x.reshape(5, 6)
print("Sequence of integers from 0-30 with steps of 5\n",array)

a1 = n.array([[5, 6], [7, 8]])
x = a1.flatten()
print("Flatten array\n",x)
array = n.full((2, 2), 6.3)
print("Constant value array\n",array)
