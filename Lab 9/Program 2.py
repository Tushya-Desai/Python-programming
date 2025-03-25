def compute(n):
    value=0
    sum=0
    for x in range(1,n+1):
        value=value*10+n
        sum+=value
    return sum
a=int(input("Enter a number:"))
sum=compute(a)
print("The answer is =",sum)
