
import tkinter as tk
from functools import partial

def add(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return

def subtract(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="Result is %d" % result)
    return

 
def multiply(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result is %d" % result)
    return

def divide(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)/int(num2)
    label_result.config(text="Result is %f" % result)
    return

def powers(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result=1
    for i in range(int(num2)):
        result = result*int(num1)
    label_result.config(text="result is %d" % result)
    return

def percentage(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = ((int(num1)/int(num2))*100)
    label_result.config(text="Result is %f" % result)
    return
    
    
root = tk.Tk()
root.geometry('800x400+200+400')
root.title('Simple Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()
 
labelTitle = tk.Label(root, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter another number").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=8, column=2)
 
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
add = partial(add, labelResult, number1, number2)
subtract = partial(subtract, labelResult, number1, number2)
multiply = partial(multiply, labelResult, number1, number2)
divide = partial(divide, labelResult, number1, number2)
powers = partial(powers, labelResult, number1, number2)
percentage = partial(percentage, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Add", command=add).grid(row=3, column=0)
C2 = tk.Button(root,text="Subtract", command=subtract).grid(row=3, column=6)
C3 = tk.Button(root,text="Multiply", command=multiply).grid(row=5, column=0)
C4 = tk.Button(root,text="Divide", command=divide).grid(row=5, column=6)
C5 = tk.Button(root,text="Power", command=powers).grid(row=6, column=0)
C6 = tk.Button(root,text="Percentage", command=percentage).grid(row=6, column=6)
root.mainloop()


