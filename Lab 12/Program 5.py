class Time():
    def __init__(self,hrs=0,min=0,sec=0):
        self.sec=sec
        self.min=min
        self.hrs=hrs
    def __add__(self,x):
        t_sec=self.sec+x.sec
        t_min=self.min+x.min
        t_hrs=self.hrs+x.hrs
        return(t_hrs+t_min/60+t_sec/3600)
    def __sub__(self,x):
        t_sec=abs(self.sec-x.sec)
        t_min=abs(self.min-x.min)
        t_hrs=abs(self.hrs-x.hrs)
        return(t_hrs+t_min/60+t_sec/3600)
obj1=Time(1,47,60)
obj2=Time(1,46,60)
obj3=obj1+obj2
print(obj3)
obj4=obj1-obj2
print(obj4)