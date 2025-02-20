l=[(101,"Amit",35,"HR",100000),(102,"Mantra",25,"IT",120000),(103,"Jeel",23,"Mkt",500000)]
l1=[]
l2=[]
l3=[]
department=(("HR","Human Resource","F-block"),("IT","Information Technology","C-Block"),("Mkt","Marketing","D-Block"))
print("The main list =",l)
while True:
    print("1 == Filter Employee Name by Department")
    print("2 == Sort Employee by salary")
    print("3 == Get the employee with highest salary")
    print("4 == Update the salary of employee")
    print("5 == Department Details")
    print("6 == Exit")
    c=int(input("Enter your choice:"))
    if c==1:
        t=input("Enter the name of department:")
        for ele in l:
            if ele[3]==t:
                l1.append(ele)
        print("The people working in",t,"are =",l1)
    elif c==2:
        l2 = [i[1] for i in l]
        l2.sort()
        for j in l2:
            for i in l:
                if(isinstance(i,tuple)):
                    if(j==i[1]):
                        l3.append(i)
        print("Original list =",l)    
        print("Salary order = ",l3)
    elif c==3:
        l=len(l3)
        print("The highest salary employee =",l3[l-1])
    elif c==4:
        t=int(input("Enter the employee ID whose salary you want to change:"))
        check=0
        for ele in l:
            if (ele[0]==t):
                sal=int(input("Enter new salary :"))
                l4=list(l[check])
                l4[4]=sal
                l[check]=tuple(l4)
            check+=1
        print("The new list is =",l)
    elif c==5:
        t=input("Enter which department details you want:")
        for x in department:
            if t==x[0]:
                print("The detail of the department are ")
                print("Full form =",x[1])
                print("Location",x[2])
    elif c==6:
        break
    else:
        print("Invalid Choice")



    
