def lis_turple(n):
    l=[]
    for x in range(1,n+1):
        p=1
        l1=[]
        for y in range(1,4):
            l1.append(x**p)
            p+=1
        tuple(l1)
        l.append(l1)
    return l
a=int(input("Enter a number:"))
lis=lis_turple(a)
print("The list =",lis)
        
    
