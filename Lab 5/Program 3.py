import random
l=[]
n=0
while(n<10):
    k=random.randint(1,20)
    l.append(k)
    n+=1
print("Original=",l)
l1=[]
for x in range(0,len(l)):
    for y in range(x+1,len(l)):
        if(l[x]==l[y]):
            break
    else:
        l1.append(l[x])
print("The non duplicate list =",l1)
            
            
