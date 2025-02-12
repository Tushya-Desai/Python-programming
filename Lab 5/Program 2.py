import random
l=[]
n=0
while(n<20):
    l.append(random.randint(1,20))
    n+=1
print("list is =",l)
a=int(input("Enter a number:"))
m=0
for y in l:
    if(y==a):
        print("One of the position is =",m)
    m+=1

