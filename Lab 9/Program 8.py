def convert(n):
    s=set()
    string=""
    for x in n:
        s.add(x)
    l=list(s)
    l.sort()
    for y in l:
        string+=y
    return string
a=input("Enter a String :")
str1=convert(a)
print("The sorted string is :",str1)
