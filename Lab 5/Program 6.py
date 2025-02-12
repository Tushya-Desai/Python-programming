l=[]
l1=[]
a=int(input("How many elements you want to enter:"))
for x in range(a):
    k=int(input("Enter temperature value in farenheit:"))
    c=5*(k-32)/9
    l.append(k)
    l1.append(c)
print("The farenheit list =",l)
print("The celsius list =",l1)
