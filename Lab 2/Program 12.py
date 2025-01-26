x=int(input("Enter x coordinate of centre:"))
y=int(input("Enter y coordinate of centre:"))
r=int(input("Enter radius of cirlce:"))
x1=int(input("Enter x1 coordinate:"))
y1=int(input("Enter y1 coordinate:"))
l=((x-x1)**2+(y-y1)**2)
if(l>(r**2)):
    print("The point(",x1,y1 ,")is outside the circle")
elif(l==(r**2)):
    print("The point(",x1,y1 ,")is on the circle")
else:
    print("The point(",x1,y1 ,")is inside the circle")
