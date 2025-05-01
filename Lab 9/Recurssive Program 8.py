a=input("Enter a string:")
def length(a):
    if(a!=""):
        return 1+length(a[1:])
    else:
        return 0
print("The length of the string is =",length(a))
