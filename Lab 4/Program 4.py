a=int(input("Enter a number:"))
if(a==2):
    print(a,"is a prime number")
else:
    for x in range(2,a):
        if(a%x==0):
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")
for x in range(1,a):
    if(x*x==a):
        print(a,"is a perfect number")
        break
else:
    print(a,"is not a perfect number")
    
b=a
temp=0
while(b!=0):
    rem=b%10
    temp=temp+rem**3
    b=b//10
if(temp==a):
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")
    
b=a
temp=0
while(b!=0):
    rem=b%10
    temp=temp*10+rem
    b=b//10
if(temp==a):
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")
 
