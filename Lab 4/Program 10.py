a=int(input("Enter 1st starting number:"))
b=int(input("Enter 2nd starting number:"))
c=int(input("Enter number of terms you want:"))
for x in range(1,c+1):
    sum=a+b
    a=b
    b=sum
    print(a)
    
