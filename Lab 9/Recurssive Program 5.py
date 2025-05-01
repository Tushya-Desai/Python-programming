a=int(input("Enter the base number:"))
b=int(input("Enter the power number:"))
def power(a,b,i=1):
    if(i==b):
        return a
    else:
        return a*power(a,b,i+1)
print(power(a,b))
    
