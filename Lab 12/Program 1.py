class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
    def printnum(self):
        if(self.i>=0):
            print(self.r,"+ i",self.i)
        else:
            print(self.r,"- i",-self.i)
    def __add__(self,x):
        a=x.r+self.r
        b=x.i+self.i
        return Complex(a,b)
    def __sub__(self,x):
        a=self.r-x.r
        b=self.i-x.i
        return Complex(a,b)
    def __mul__(self,x):
        a=self.r*x.r-self.i*x.i
        b=self.r*x.i+self.i*x.r
        return Complex(a,b)
    def __truediv__(self,x):
        a=(self.r*x.r+self.i*x.i)/(x.r**2+x.i**2)
        b=(-(self.r*x.i-self.i*x.r))/(x.r**2+x.i**2)
        return Complex(a,b)
        
obj1=Complex(2,4)
obj2=Complex(2,4)
obj3=obj1+obj2
obj3.printnum()
obj4=obj1-obj2
obj4.printnum()
obj5=obj1*obj2
obj5.printnum()
obj6=obj1/obj2
obj6.printnum()
