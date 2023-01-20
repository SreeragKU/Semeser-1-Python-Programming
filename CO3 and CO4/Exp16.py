import Graphics.Rectangle as r
import Graphics.Circle as c
import Graphics.ThreeD_Graphics.Cuboid as cb
import Graphics.ThreeD_Graphics.Sphere as s
x=int(input("Enter the length of the rectangle: "))
y=int(input("Enter the breadth of the rectangle: "))
r.area(x,y)
r.Perimeter(x,y)
rd=int(input("\nEnter the length of the rectangle: "))
c.area(rd)
c.Perimeter(rd)
x=int(input("\nEnter the length of the rectangle: "))
y=int(input("Enter the width of the rectangle: "))
z=int(input("Enter the height of the rectangle: "))
cb.area(x,y,z)
cb.Perimeter(x,y,z)
rd=int(input("\nEnter the length of the rectangle: "))
s.area(rd)
s.Perimeter(rd)
