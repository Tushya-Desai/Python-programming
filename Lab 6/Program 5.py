a=[("Akshat 1",5),("Neel 1",2),(),("Neel","to take 5 rupees",-5),(),("Devansh",-2.5)]
print("Original list =",a)
for x in a:
    if(len(x)==0):
        a.remove(x)
print("Clean list =",a)
