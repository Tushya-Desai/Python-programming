class matrix():
    def __init__(self,l):
        if l==0:
            self.l=[[0,0,0],[0,0,0],[0,0,0]]
        else:
            self.l=l
    def printm(self):
        print(self.l)
    def __add__(self,m2):
        m1=matrix(0)
        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                m1.l[i][j]=self.l[i][j]+m2.l[i][j]
        return m1
    def __mul__(self,m2):
        m1=matrix(0)
        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                sum1=0
                for a in range(len(self.l)):
                    sum1+=self.l[i][a]*m2.l[a][j]
                m1.l[i][j]=sum1
        return m1
    def transpose(self):
        m1=matrix(0)
        for i in range(len(self.l)):
            for j in range(len(self.l[0])):
                m1.l[i][j]=self.l[j][i]
        return m1

obj1=matrix([[3,1,1],[2,5,5],[4,6,1]])
obj1.printm()
obj2=matrix([[5,3,2],[7,6,1],[4,4,4]])
obj2.printm()
obj3=obj1+obj2
obj3.printm()
obj4=obj1*obj2
obj4.printm()
obj5=matrix.transpose(obj1)
obj5.printm()
