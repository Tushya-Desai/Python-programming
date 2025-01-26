for x in range(1,25):
    if(x<12):
        print(x,"A.M")
    elif(x==12):
        print(x,"A.M (Noon)")
    elif(x>12 and x<24):
        print(x-12,"P.M")
    else:
        print(x-12,"P.M (Midnight)")
