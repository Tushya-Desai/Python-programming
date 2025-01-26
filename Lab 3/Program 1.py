l=[10,20,30,40,50,60,70,80,90,100]
a=int(input("Enter the value u want to search in the list:"))
for x in l:
    if(a==x):
        print(a,"is present")
        break
else:
    print(a,"is not present")
