def average(l,i=0):
    if(i==len(l)-1):
        return l[i]
    elif(i==0):
        return (l[i]+average(l,i+1))/len(l)
    else:
        return (l[i]+average(l,i+1))
l=[10,35,31,22,41,50,7,135]
print('The average of the numbers is =',average(l))
