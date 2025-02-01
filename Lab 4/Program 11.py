a=int(input("Enter angle in degree:"))
b=a*3.14159/180
sum=0
def fact(n):
    l=1
    for x in range(n,0,-1):
        l=l*x
    return l
rem=1
for i in range(0,50):
    rem=((-1)**i*b**(2*i+1)/fact(2*i+1))
    sum=sum+rem
print("Sin(",a,") =")
print(sum)
