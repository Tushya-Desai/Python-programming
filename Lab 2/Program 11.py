x1=int(input("Enter 1st x coordinate:"))
y1=int(input("Enter 1st y coordinate:"))
x2=int(input("Enter 2nd x coordinate:"))
y2=int(input("Enter 2nd y coordinate:"))
x3=int(input("Enter 3rd x coordinate:"))
y3=int(input("Enter 3rd y coordinate:"))
s1=((x2-x1)**2+(y2-y1)**2)**(1/2)
s2=((x3-x2)**2+(y3-y2)**2)**(1/2)
s3=((x3-x1)**2+(y3-y1)**2)**(1/2)
length=s1+s2
if(length==s3):
    print("They are collinear")
else:
    print("They are not collinear")
