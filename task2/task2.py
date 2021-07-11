from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys
#y=math.pow(x,2)
#y=x*x
#y=x^2
version = 0.1
 
root = Tk()
root.title("Calculator")
 
#calculator logic
def calc(key):
    global memory
    if key == "=":
#exclude writing letters
        str1 = "-+0123456789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#score
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
 
#clear field
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "sin":
        sin=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.sin(float(sin)))
    elif key == "cos":
        cos=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.cos(float(cos)))
    elif key == "tan":
        tan=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.tan(float(tan)))
    elif key == "ctg":
        ctg=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.cos(float(cos))/math.sin(float(sin)))
    elif key == "log":
        log=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.log(float(log)))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
 
 
#buttons
bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=",
"0", ".", "±",  "C",
"sin", "cos", "tan", "ctg", "log"
 
 
]
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)
 
root.mainloop()