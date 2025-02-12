import random 
l1=[]
l2=[]
for x in range(10):
    k=random.randint(1,25)
    l1.append(k)
for y in range(10):
    k=random.randint(1,25)
    l2.append(k)
l3=[i for i in l1 if i not in l2]
print("The first list is :",l1)
print("The second list is :",l2)
print("The modified list is :",l3)
