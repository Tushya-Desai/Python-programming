f1=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile6a.txt",'r')
f2=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile6b.txt",'r')
f3=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile6c.txt",'w')
m=f1.readlines()
n=f2.readlines()
a=len(m)
b=len(n)
if(a>b):
    for x in range(b):
        f3.write(m[x])
        f3.write(n[x])
    for y in range(b,a):
        f3.write("\n"+m[y])
if(b>a):
    for x in range(a):
        f3.write(m[x])
        f3.write(n[x])
    for y in range(a,b):
        f3.write("\n"+n[y])      
f1.close()
f2.close()
f3.close()
