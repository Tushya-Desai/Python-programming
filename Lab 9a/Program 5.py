l=['Tushya Desai','Mantra Patel','Jeel Shah','Mittal Suthar','Divyam Patel','Akshat Jariwala']
def length(n):
    return 1 if len(n)>8 else 0
l1=filter(length,l)
print(list(l1))
