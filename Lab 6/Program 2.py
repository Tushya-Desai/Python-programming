l=[(1,"abc",18),(2,"def",19),(3,"ghi",18),(4,"jkl",17),(5,"mno",18)]
Lname=[]
Lrollno=[]
Lage=[]
for x in l:
    for a in range(3):
        if(a==0):
            Lrollno.append(x[a])
        elif(a==1):
            Lname.append(x[a])
        else:
            Lage.append(x[a])
print("The roll numbers are =",Lrollno)
print("The names are =",Lname)
print("The age are =",Lage)
            
    
