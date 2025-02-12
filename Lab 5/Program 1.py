import random
l=[]
l1=[]
n=0
while(n<5):
    k=random.randint(1,100)
    if(k%2==1):
        l.append(k)
        n+=1
print("The random odd number list =",l)
n=0
while(n<4):
    k=random.randint(1,100)
    if(k%2==0):
        l1.append(k)
        n+=1
print("The random even number list =",l1)
l.insert(2,l1)
l.pop(3)
print("The 3rd list =",l)

l2=[]
for x in l:
    print(x)
    l2.extend([x])
print("The flatterned list =",l2)
l2.sort()
print("The sorted listed =",l2)
