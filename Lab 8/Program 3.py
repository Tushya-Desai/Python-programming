l=[]
for x in range(5):
    k=input("Enter a name :")
    l.append(k)
s={i for i in l}
print("Main set =",s)
while True:
    print("1 == Modify a name")
    print("2 == Delete a name")
    print("3 == Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        l=list(s)
        t=input("Enter name which you want to change:")
        n=input("Enter new name:")
        check=0
        for x in l:
            if x==t:
                l[check]=n
            check+=1
        s=set(l)
        print("The new set =",s)
    elif c==2:
        l=list(s)
        t=input("Enter name which you want to delete:")
        for x in l:
            if x==t:
                l.remove(t)
        s=set(l)
    elif c==3:
        break
    else:
        print("Invalid Choice")
        
                
