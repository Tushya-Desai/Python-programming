n=int(input("Enter total number of objects:"))
r=int(input("Enter number of object to be selected:"))
l=1
m=1
k=1
for x in range(n,0,-1):
    l=l*x
for y in range(n-r,0,-1):
    m=m*y
for z in range(r,0,-1):
    k=k*z
nPr=l/m
print("The nPr =",nPr)
nCr=l/(m*k)
print("The nCr =",nCr)
