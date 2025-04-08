l=[1,2,3,4,5,6]
l1=[6,5,4,3,2,1]
def sumation(a,b):
    return a+b
l2=map(sumation,l,l1)
print(list(l2))
