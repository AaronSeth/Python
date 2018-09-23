import statistics


def mysum(list1):
    sumo = 0
    for i in range(len(list1)):
                   sumo = sumo + list1[i]
    print(sumo)               

def myave(list1):
    sumoo = 0 
    for a in range(len(list1)):
        sumoo = sumoo + list1[a]
    ave = sumoo/len(list1)
    print(ave)

def mymedian(data):
    a = data.sort()
    a = statistics.median(data)
    print(a)

def mytimestable(x):
    result = []
    j = 1
    while j <= 12:
        b = j * x
        j = j + 1
        result.append(b)
    print(result)

def myfactor(y):
    result1 = []
    for u in range(1, y + 1):
       if y % u == 0:
           result1.append(u)
    print(result1)
    
def myprimelist(z):
    result2 = []
    for k in range(2, z):
        prime = True
        for g in range(2, k):
            if k%g == 0:
                prime = False       
        if prime:
            result2.append(k)
    print(result2)
    



        
        
