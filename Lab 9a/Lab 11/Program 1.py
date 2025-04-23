while(True):
    try:
        a=int(input("Enter a number:"))
        break
    except ValueError:
        print("It is not a integer")
print("The number you entered is =",a)
        
