def count_vowel(a,v=['a','e','i','o','u'],i=1,count=0):
    if(i==len(a)):
        if a[i-1] in v :
            return 1
        else:
            return 0
    else:
        if a[i-1] in v:
            return 1+count_vowel(a,v,i+1,count)
        else:
            return count_vowel(a,v,i+1,count)
a=input('Enter a string:')
print("The number of times vowels occure in the string is =",count_vowel(a))
