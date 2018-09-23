import tkinter as tk
from functools import partial


def cashconverter(label_result, a1,b1):
    a=(a1.get())
    b=(b1.get())
    c=float(a)*float(b)
    label_result.config(text="Rupees %f" % c)
    return

root = tk.Tk()
root.geometry('800x400+200+400')
root.title('Cash Converter')

n1 = tk.StringVar()
n2 = tk.StringVar()

labelTitle=tk.Label(root, text="Cash Conveter").grid(row=0, column=2)
labeln1=tk.Label(root, text="Australian Dollar", fg=('red'), bg=('blue')).grid(row=2, column=0)
labeln2=tk.Label(root, text="Buying rate of Inr", fg=('white'), bg=('orange')).grid(row=3, column=0)

entryNum1 = tk.Entry(root, textvariable=n1).grid(row=2, column=2)
entryNum2 = tk.Entry(root, textvariable=n2).grid(row=3, column=2)
labelResult=tk.Label(root)
labelResult.grid(row=8, column=2)

cashconverter = partial(cashconverter, labelResult, n1, n2)
buttonCal = tk.Button(root, text="Amount of Inr", fg=('white'), bg=('orange'), command=cashconverter).grid(row=3, column=3)

def InrtoAud(label_result, f1,c1):
    f=(f1.get())
    c=(c1.get())
    d=float(f)*float(c)
    label_result.config(text="AUD %f" % d)
    return

a1 = tk.StringVar()
a2 = tk.StringVar()

labelTitle=tk.Label(root, text="Cash Conveter (Inr-Aud)").grid(row=5, column=2)
labela1=tk.Label(root, text="Indian Rupee", fg=('white'), bg=('orange')).grid(row=6, column=0)
labela2=tk.Label(root, text="Selling Rate of Inr to Aud", fg=('red'), bg=('blue')).grid(row=7, column=0)

entryNum3 = tk.Entry(root, textvariable=a1).grid(row=6, column=2)
entryNum4 = tk.Entry(root, textvariable=a2).grid(row=7, column=2)
labelResult=tk.Label(root)
labelResult.grid(row=9, column=2)

InrtoAud = partial(InrtoAud, labelResult, a1, a2)
buttonCal = tk.Button(root, text="Amount of Aud",fg=('red'), bg=('blue'), command=InrtoAud).grid(row=7, column=3)

root.mainloop()
