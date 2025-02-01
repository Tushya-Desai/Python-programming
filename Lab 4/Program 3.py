a=input("Enter a string:")
num=0
alp=0
for x in a:
    if(ord(x)>=48 and ord(x)<=57):
        num+=1
    else:
        alp+=1
print("The number of alphabet =",alp)
print("The number of digits =",num)
