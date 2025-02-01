def string_remover(a,b):
    z =""
    l=len(a)
    for x in range(0,l+1):
        for y in range(0,l+1):
            if(b==a[x:y]):
                z=z+a[0:x]
                z=z+a[y:l]
    return z
a=input("Enter a parent string:")
b=input("Enter a string to remove:")
print("The new string =",string_remover(a,b))
