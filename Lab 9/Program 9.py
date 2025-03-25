def count_alpha_digit(n):
    c_alpha=0
    c_num=0
    for x in n:
        y=ord(x)
        if(y>=65 and y<=90 or y>=97 and y<=122):
            c_alpha+=1
        elif(y>=48 and y<=57):
            c_num+=1
    dict1={"Alphabet":c_alpha,"Numbers":c_num}
    return dict1
a=input("Enter a String:")
d=count_alpha_digit(a)
print(d)
