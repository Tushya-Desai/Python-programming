def count_lower_upper(n):
    c_upper=0
    c_lower=0
    for x in n:
        y=ord(x)
        if y>=65 and y<=90:
            c_upper+=1
        elif y>=97 and y<=122:
            c_lower+=1
    d1={"Upper":c_upper,"Lower":c_lower}
    return d1
a=input("Enter a String:")
dictionary=count_lower_upper(a)
print(dictionary)
