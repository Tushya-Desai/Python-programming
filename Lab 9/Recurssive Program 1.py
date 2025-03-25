def root_checker(n,i=0,roots=[]):
    l=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    while i < len(l):
        if n % l[i] == 0:
            roots.append(l[i])
            n/=l[i]
            return root_checker(n, i, roots)
        i += 1
    return roots
a=int(input("Enter a positive number:"))
l=root_checker(a)
print("The prime factors are:",l)
