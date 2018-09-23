import math

principle=int(input("what is you principle amount:"))
rate=float(input("what is your yearly interest rate:"))
time=int(input("how much time do you have to pay off the loan:"))
formula=str(input("what formula would you like to calculate: comi or simi:"))

def comsim(p,r,t,f):
    if f=="simi":
        print(p*r*t)

    if f=="comi":
        print(p*(1+r)**t)

comsim(principle,rate,time,formula)
    
