income=int(input("What is your base yearly icome?"))

def tax(i):
    taxi=0
    if i<=18200:
        taxi=0
    else:
        if i>=18201 and i<=37000:
            taxi=(i-18201)*0.19
        else:
            if i>=37001 and i<=87000:
                taxi=3572+((i-37000)*0.325)
            else:
                if i>=87001 and i<=180000:
                    taxi=19822+((i-87000)*0.37)
                else:
                    if i>=180001:
                        taxi=54232+((i-180000)*0.45)
    print(taxi)                    
tax(income)

