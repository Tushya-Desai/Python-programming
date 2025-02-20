l=[]
n=int(input("How many elements you want to enter :"))
for x in range(n):
    k=input("Enter element :")
    l.append(k)
print("The original list =",l)
s={i.upper() for i in l}
print("The set =",s)
