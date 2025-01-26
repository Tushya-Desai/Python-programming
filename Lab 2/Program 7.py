a=int(input("Enter a number:"))
if(a%100==0):
    if(a%400==0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
else:
    if(a%4==0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
