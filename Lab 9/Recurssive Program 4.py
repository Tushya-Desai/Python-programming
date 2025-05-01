import random
l=[]
while(len(l)<10):
    k=random.randint(0,30)
    l.append(k)
def reverse(l):
    if not l:
        return []
    else:
        return [l[-1]]+reverse(l[:-1])
print("The original list is",l)
print("The reverse list is",reverse(l))
