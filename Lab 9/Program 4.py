def sum_avg(m1,m2,m3,m4,m5):
    sum1=m1+m2+m3+m4+m5
    avg=sum1/5
    return(avg,sum1)
a=int(input('Enter 1st marks:'))
b=int(input('Enter 2nd marks:'))
c=int(input('Enter 3rd marks:'))
d=int(input('Enter 4th marks:'))
e=int(input('Enter 5th marks:'))
avg,sum1=sum_avg(a,b,c,d,e)
print("The sum=",sum1)
print("The Average=",avg)
    
