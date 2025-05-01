class solid():
    def __init__(self,l=0,b=0,h=0,a=0):
        self.l=l
        self.b=b
        self.h=h
        self.a=a
    def square(self):
        if(self.b==1):
            Perimeter=4*self.l
            return Perimeter
        else:
            Area=self.l**2
            return Area
    def rectangle(self):
        if(self.h==1):
            Perimeter=2*(self.l+self.b)
            return Perimeter
        else:
            Area=self.l*self.b
            return Area
    def circle(self):
        if(self.b==1):
            Perimeter=2*3.14*self.l
            return Perimeter
        else:
            Area=3.14*(self.l**2)
            return Area
    def triangle(self):
        if(self.a==1):
            Perimeter=self.l+self.b+self.h
            return Perimeter
        else:
            s=(self.l+self.b+self.h)/2
            Area=(s*(s-self.l)*(s-self.b)*(s-self.h))**0.5
            return Area
while (True):
    print("1-Perimeter")
    print("2-Area")
    print("3-Exit")
    a=int(input('Enter your choice:'))
    if(a==3):
        break
    elif(a!=1 and a!=2):
        print("Invalid choice")
        continue
    print("1-Square")
    print("2-Rectangle")
    print("3-Circle")
    print("4-Triangle")
    c=int(input("Enter your choice:"))
    if c==1:
        s=int(input("Enter side of the square:"))
        obj1=solid(s,a)
        print(obj1.square())
    if c==2:
        l=int(input("Enter length of the rectangle:"))
        b=int(input("Enter breadth of the rectangle:"))
        obj1=solid(l,b,a)
        print(obj1.rectangle())
    if c==3:
        r=int(input("Enter radius of the circle:"))
        obj1=solid(r,a)
        print(obj1.circle())
    if c==4:
        s1=int(input("Enter side 1 of the triangle:"))
        s2=int(input("Enter side 2 of the triangle:"))
        s3=int(input("Enter side 3 of the triangle:"))
        obj1=solid(s1,s2,s3,a)
        print(obj1.triangle())