import random
l=[]
l1=[]
l2=[]
for x in range(0,30):
    k=random.randint(-50,50)
    l.append(k)
    if(k>=0):
        l1.append(k)
    else:
        l2.append(k)
print("The main list =",l)
print("The positive list =",l1)
print("The negative list =",l2)
