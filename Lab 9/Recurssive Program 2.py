def binary_converter(n,l=[]):
    p,i=n,-1
    while p!=0:
        i+=1
        m=2**i
        r=p-m
        if r<m:
            break
    print(i)
    for x in range(i,-1,-1):
        if n>(2**x):
            n=n-(2**x)
            l.append(1)
        else:
            l.append(0)
    return l
a=int(input("Enter a number:"))
l=binary_converter(a)
str=""
for y in l:
    str+=char(y)
    
if(a%2==0):
    str+="0"
else:
    str+="1"
print("The binary code for the number =",str)
