class string():
    def __init__(self,s):
        self.s=s
    def prints(self):
        print(self.s)
    def __iadd__(self,x):
        self.s=self.s+x.s
        return string(self.s)
    def tolower(self):
        return self.s.lower()
    def toupper(self):
        return self.s.upper()
obj1=string("Tushya")
obj2=string("Desai")
obj1+=obj2
print(obj1.tolower())
print(obj1.toupper())
