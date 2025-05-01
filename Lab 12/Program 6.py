class Date():
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    def __eq__(self,x):
        return True if(self.d==x.d and self.m==x.m and self.y==x.y) else False
obj1=Date(*[31,3,2007])
obj2=Date(*[31,2,2007])
print(obj1==obj2)
