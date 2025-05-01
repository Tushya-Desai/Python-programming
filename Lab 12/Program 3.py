class solid():
    def __init__(self,l=0,b=0,h=0,a=0):
        self.l=l
        self.b=b
        self.h=h
        self.a=a
    def cube(self):
        if(self.b==1):
            SA=6*(self.l**2)
            return SA
        else:
            vol=self.l**3
            return vol
    def cuboid(self):
        if(self.a==1):
            SA=2*(self.l*self.b+self.l*self.h+self.b*self.h)
            return SA
        else:
            vol=self.l*self.b*self.h
            return vol
    def sphere(self):
        if(self.b==1):
            SA=4*3.14*(self.l**2)
            return SA
        else:
            vol=4*3.14*(self.l**3)/3
            return vol
    def cylinder(self):
        if(self.h==1):
            SA=2*3.14*self.l*(self.l+self.b)
            return SA
        else:
            vol=3.14*(self.l**2)*self.b
            return vol
while (True):
    print("1-Surface Area")
    print("2-Volume")
    print("3-Exit")
    a=int(input('Enter your choice:'))
    if(a==3):
        break
    elif(a!=1 and a!=2):
        print("Invalid choice")
        continue
    print("1-Cube")
    print("2-Cuboid")
    print("3-Sphere")
    print("4-Cylinder")
    c=int(input("Enter your choice:"))
    if c==1:
        s=int(input("Enter side of the cube:"))
        obj1=solid(s,a)
        print(obj1.cube())
    if c==2:
        l=int(input("Enter length of the cuboid:"))
        b=int(input("Enter length of the cuboid:"))
        h=int(input("Enter length of the cuboid:"))
        obj1=solid(l,b,h,a)
        print(obj1.cuboid())
    if c==3:
        r=int(input("Enter radius of the sphere:"))
        obj1=solid(r,a)
        print(obj1.sphere())
    if c==4:
        r=int(input("Enter radius of the cylinder:"))
        h=int(input("Enter height of the cylinder:"))
        obj1=solid(r,h,a)
        print(obj1.cylinder())
