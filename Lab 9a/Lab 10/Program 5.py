fp=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile4.txt",'r')
fp1=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile5.txt",'w')
for l in fp.readline():
    s=l.upper()
    fp1.write(s)
fp.close()
fp1.close()
print("your data transfer successfully!")
