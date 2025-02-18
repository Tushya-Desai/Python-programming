student = [("b1","b2"),"g1",("b3",),"g2",("b4","b5"),"g3"]
boys = 0
girls=0
for i in student:
    if(isinstance(i,tuple)):
        for x in i:
            boys += 1
    else:
        girls+=1
print("Students = : ",student)
print("Number of boys =: ",boys)
print("Number of boys =: ",girls)
