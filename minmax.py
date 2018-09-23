
a=int(input("enter number 'a': "))
b=int(input("enter another number 'b': "))
c=int(input("enter the last number 'c': "))

def maxx(a1,b1,c1):
    if(a1>b1):
        if(a1>c1):
            print("a is the largest number")
        else:
            print("c is the largest number")
    else:
        if(b1>c1):
            print("b is the lagest number")
        else:
            print("c is the largest number")
        
maxx(a,b,c)

