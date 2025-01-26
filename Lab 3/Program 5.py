print("The pythagorean triplets are =")
for z in range(1,31):
    for y in range(1,31):
        for x in range(1,31):
            l=x**2+y**2
            if(l==(z**2) and x<y):
                print(x,y,z)
            
