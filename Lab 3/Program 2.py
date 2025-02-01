def upper(str):
    z =""
    for i in str:
        y = ord(i)
        if(y<=123 and y>=97):
            y = y - 32
        z=z+chr(y)
    return z
def lower(str1):
    z1 =""
    for i in str1:
        y1 = ord(i)
        if(y1<=90 and y1>=65):
            y1 = y1 + 32
        z1=z1+chr(y1)
    return z1
z=input("Enter a lower case string:")
z1=input("Enter a upper case string:")
print("The upper case =",upper(z))
print("The lower case =",lower(z1))
