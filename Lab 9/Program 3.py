def create_array(r,c,h,n):
    l2=[]
    for z in range(h):
        l=[]
        for x in range(r):
            l1=[]
            for y in range(c):
                l1.append(n)
            l.append(l1)
        l2.append(l)
    return l2

a=int(input("Enter number of rows:"))
b=int(input("Enter number of column:"))
c=int(input("Enter number of depth:"))
d=int(input("Enter element:"))
list1=create_array(a,b,c,d)
print("The list is",list1)
