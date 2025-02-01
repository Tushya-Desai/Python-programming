def vowel_checker(a):
    b=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for x in a:
        if x in b:
            count+=1
    return count
a=input("Enter a string:")
b=vowel_checker(a)
print("The number of times vowels occured is =",b)

