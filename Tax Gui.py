
import tkinter as tk
from functools import partial

def tax(label_result, label_result2, n1):
    num = int(n1.get())
    taxi=0
    if num<=18200:
        taxi=0
    else:
        if num>=18201 and num<=37000:
            taxi=(num-18201)*0.19
        else:
            if num>=37001 and num<=87000:
                taxi=3572+((num-37000)*0.325)
            else:
                if num>=87001 and num<=180000:
                    taxi=19822+((num-87000)*0.37)
                else:
                    if num>=180001:
                        taxi=54232+((num-180000)*0.45)
    label_result.config(text="Your annual tax is is %f" % taxi)
    label_result2.config(text="Your hometaking is %f" %(num-taxi))
    return

def mon(label_result, label_result2, n1):
    num = int(n1.get())
    taxi=0
    if num<=18200:
        taxi=0
    else:
        if num>=18201 and num<=37000:
            taxi=(num-18201)*0.19
        else:
            if num>=37001 and num<=87000:
                taxi=3572+((num-37000)*0.325)
            else:
                if num>=87001 and num<=180000:
                    taxi=19822+((num-87000)*0.37)
                else:
                    if num>=180001:
                        taxi=54232+((num-180000)*0.45)
    label_result.config(text="Your monthly tax is is %f" % (taxi/12))
    label_result2.config(text="Your montyhly hometaking is %f" %((num-taxi)/12))
    return

def week(label_result, label_result2, n1):
    num = int(n1.get())
    taxi=0
    if num<=18200:
        taxi=0
    else:
        if num>=18201 and num<=37000:
            taxi=(num-18201)*0.19
        else:
            if num>=37001 and num<=87000:
                taxi=3572+((num-37000)*0.325)
            else:
                if num>=87001 and num<=180000:
                    taxi=19822+((num-87000)*0.37)
                else:
                    if num>=180001:
                        taxi=54232+((num-180000)*0.45)
    label_result.config(text="Your weekly tax is is %f" % (taxi/52))
    label_result2.config(text="Your weekly hometaking is %f" %((num-taxi)/52))
    return

             
root = tk.Tk()
root.geometry('800x400+200+400')
root.title('Tax Calculator')

number1 = tk.StringVar()

labelTitle = tk.Label(root, text="Tax Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter your base salary").grid(row=1, column=0)
labelResult = tk.Label(root)
labelResult2 = tk.Label(root)
labelResult.grid(row=9, column=2)
labelResult2.grid(row=10, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
tax = partial(tax, labelResult, labelResult2, number1)
mon = partial(mon, labelResult, labelResult2, number1)
week = partial(week, labelResult, labelResult2, number1)
buttonCal = tk.Button(root, text="Calculate Annual Tax", command=tax).grid(row=0, column=3)
B1 = tk.Button(root, text="Calculate Monthly Tax", command=mon).grid(row=1, column=3)
B2 = tk.Button(root, text="Calculate Weekly Tax", command=week).grid(row=0, column=4)
root.mainloop()              
                 
