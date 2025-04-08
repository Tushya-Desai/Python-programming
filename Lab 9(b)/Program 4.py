lst=['madam','Python','malayalam',12321]
def palindrome(n):
    if(isinstance(n,int)==True):
        n=str(n)
    l=len(n)    
    s=""
    for x in range(l):
        s=s+n[l-x-1]
    return 1 if s==n else 0
l=filter(palindrome,lst)
print(list(l))
