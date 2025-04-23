l=['a','an','the']
f1=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile8a.txt",'r')
f2=open("C:\Semester 2\Computer(Python)\Lab 10\Myfile8b.txt",'w')
for x in f1:
    new=" ".join(y for y in x.split() if y not in l)
    f2.write(new+"\n")
f1.close()
f2.close()
