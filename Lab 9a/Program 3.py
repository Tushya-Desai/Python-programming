import random
l=[]
for x in range(10):
    k=random.randint(-15,15)
    l.append(k)
def sq(n):
    return n*n
l1=map(sq,l)
print(list(l1))
