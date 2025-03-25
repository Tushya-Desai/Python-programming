def ispalindrome(n):
    l=len(n)    
    s=""
    for x in range(l):
        s=s+n[l-x-1]
    return s
a=input("Enter a String:")
rev=ispalindrome(a)
if a==rev:
    print(a,"is Palindrome")
else:
    print(a,"is not Palindrome")
