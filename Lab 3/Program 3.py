def string_checker(a,b):
    for x in range(0,len(a)+1):
        for y in range(0,len(a)+1):
            if(b==a[x:y]):
                print(b,"is present in the parent string")
                break
a=input("Enter the parent string:")
b=input("Enter the small string:")
string_checker(a,b)
