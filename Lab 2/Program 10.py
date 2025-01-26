l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
area=l*b
perimeter=2*(l+b)
print("Area=",area)
print("Perimter=",perimeter)
if(area>perimeter):
    print("The area is greater than perimeter")
else:
    print("The area is not greater than perimeter")
