a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))
if(a>b):
    if(a>c):
        if(b>c):
            print("The largest number is =",a,"The smallest number is =",c)
        else:
            print("The largest number is =",a,"The smallest number is =",b)
    else:
        print("The largest number is =",c,"The smallest number is =",b)
else:
    if(b>c):
        if(a>c):
            print("The largest number is =",b,"The smallest number is =",c)
        else:
            print("The largest number is =",b,"The smallest number is =",a)
    else:
        print("The largest number is =",c,"The smallest number is =",a)
