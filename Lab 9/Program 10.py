def frequency(p):
    n=p.upper()
    l1=[]
    l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in l:
        count_alpha=0
        for y in n:
            if x==y:
                count_alpha+=1
        l1.append(count_alpha)
    return(l,l1)
a=input("Enter a String:")
l,l1=frequency(a)
for x in range(0,len(l)):
    print("The number of times",l[x],"occured is =",l1[x])
    
