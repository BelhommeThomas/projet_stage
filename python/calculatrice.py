#library
import math
import random
from tkinter import *

#start program
cal = Tk()
cal.title("calculatrice")

#obtain info
user = Entry(cal, width=35, borderwidth=5)
user.grid(row=0, column=0, columnspan=3, padx = 10, pady=10)

#button's action
def button1():
    current = user.get()
    num = 1
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button2():
    num = 2
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button3():
    num = 3
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button4():
    num = 4
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button5():
    num = 5
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button6():
    num = 6
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button7():
    num = 7
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button8():
    num = 8
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button9():
    num = 9
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def button0():
    num = 0
    current = user.get()
    user.delete(0,"end")
    user.insert(0, str(current) + str(num))
def buttondot():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "dot"
    f_num = float(newlabel)

def buttonplus():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "addition"
    f_num = float(newlabel)
def buttonminus():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "substraction"
    f_num = float(newlabel)
def buttontimes():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "times"
    f_num = float(newlabel)
def buttondivide():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "divide"
    f_num = float(newlabel)
def buttonpower():
    newlabel = user.get()
    global f_num
    global math
    user.delete(0,"end")
    math = "power"
    f_num = float(newlabel)
def buttonequal():
    second_num = user.get()
    user.delete(0, "end")
    if(math == "addition"):
        user.insert(0, f_num + int(second_num))
    elif(math == "substraction"):
        user.insert(0, f_num - int(second_num))
    elif(math == "times"):
        user.insert(0, f_num * int(second_num))
    elif(math == "divide"):
        user.insert(0, f_num / int(second_num))
    elif(math == "power"):
        user.insert(0, f_num ** float(second_num))
    elif(math == "dot"):
        user.insert(0, f_num + (float(second_num) / 10))
def buttonclear():
    user.delete(0,"end")

#buttons and color

button_1 = Button(cal, text="1", padx=40, pady=20, command=button1, background= "#4a7a8c")
button_2 = Button(cal, text="2", padx=40, pady=20, command=button2, background= "#4a7a8c")
button_3 = Button(cal, text="3", padx=40, pady=20, command=button3, background= "#4a7a8c")
button_4 = Button(cal, text="4", padx=40, pady=20, command=button4, background= "#4a7a8c")
button_5 = Button(cal, text="5", padx=40, pady=20, command=button5, background= "#4a7a8c")
button_6 = Button(cal, text="6", padx=40, pady=20, command=button6, background= "#4a7a8c")
button_7 = Button(cal, text="7", padx=40, pady=20, command=button7, background= "#4a7a8c")
button_8 = Button(cal, text="8", padx=40, pady=20, command=button8, background= "#4a7a8c")
button_9 = Button(cal, text="9", padx=40, pady=20, command=button9, background= "#4a7a8c")
button_0 = Button(cal, text="0", padx=40, pady=20, command=button0, background= "#4a7a8c")
button_dot = Button(cal, text=".", padx=40, pady=20, command=buttondot, background= "#b4d455")
button_plus = Button(cal, text="+", padx=40, pady=20, command=buttonplus, background= "#b4d455")
button_minus = Button(cal, text="-", padx=40, pady=20, command=buttonminus, background= "#b4d455")
button_times = Button(cal, text="*", padx=40, pady=20, command=buttontimes, background= "#b4d455")
button_divide = Button(cal, text="/", padx=40, pady=20, command=buttondivide, background= "#b4d455")
button_power = Button(cal, text="^", padx=40, pady=20, command=buttonpower, background= "#b4d455")
button_equal = Button(cal, text="=", padx=135, pady=20, command=buttonequal, background= "#b4d455")
button_clear = Button(cal, text="clear", padx=80, pady=20, command=buttonclear, background= "#b23b68")

#button placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_dot.grid(row=5, column=2)
button_plus.grid(row=5, column=0)
button_minus.grid(row=5, column=1)
button_times.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_power.grid(row=6, column=2)
button_equal.grid(row=7, column=0, columnspan=3)
button_clear.grid(row=4, column=1, columnspan=2)

#end program
cal.mainloop()