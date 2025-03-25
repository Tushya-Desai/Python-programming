def create_list(l1,l2):
    s1=set(l1)
    s2=set(l2)
    s3=s1&s2
    l=list(s3)
    return l
n=int(input("How many element you want to enter:"))
l1=[]
l2=[]
print("FOR LIST 1")
for x in range(n):
    k=int(input("Enter a number:"))
    l1.append(k)
print("FOR LIST 2")
for y in range(n):
    k=int(input("Enter a number:"))
    l2.append(k)
l=create_list(l1,l2)
print("The intersection of the 2 list is =",l)
