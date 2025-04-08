def fun():
    print("hi")

def disp():
    print("dude")

def msg():
    print("howdy")

l=[fun,disp,msg]
m1=list(map(lambda x:x(),l))

    
