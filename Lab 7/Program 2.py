import random
l=[]
while len(l)<=10:
    k=random.randint(15,45)
    l.append(k)
s={i for i in l}
print("The original set =",s)
count=0
for x in s:
    if x<30:
        count+=1
l1=[]
for y in s:
    if y<35:
        l1.append(y)
s=set(l1)
print(count,"number are less than 30")
print("The new set =",s)

