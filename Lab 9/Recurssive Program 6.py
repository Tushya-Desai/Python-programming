import random
l=[]
while(len(l)<10):
    k=random.randint(-20,20)
    l.append(k)
print(l)
def sanitizer(l):
    if not l:
        return []
    else:
        if(l[0]<0):
            return [0]+sanitizer(l[1:])
        else:
            return [l[0]]+sanitizer(l[1:])
print(sanitizer(l))
        
