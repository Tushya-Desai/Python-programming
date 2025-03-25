def ispanagram(n):
    s=set()
    p=n.lower()
    for x in p:
        s.add(x)
    l=len(s)
    return l
a=input("Enter a sentance:")
l=ispanagram(a)
if l==26:
    print("It is a panagram")
else:
    print("It is not a panagram")
    
