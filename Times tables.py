numfortable=int(input("Which nuumber do you want a times table for?"))

def timet(n):
    i=1
    while(i<=12):
        p=i*n
        print(i,"*",n,"=", p)
        i=i+1
        

timet(numfortable)
