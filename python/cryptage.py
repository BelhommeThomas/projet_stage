# unfinished
# import
import random
from tkinter import *

#set lib
cy = Tk()
cy.title('crypto')
key = { 'A':0, 'B':1,
        'C':2, 'D':3, 'E':4,
        'F':5, 'G':6, 'H':7,
        'I':8, 'J':9, 'K':10,
        'L':11, 'M':12, 'N':13,
        'O':14, 'P':15, 'Q':16,
        'R':17, 'S':18, 'T':19,
        'U':20, 'V':21, 'W':22,
        'X':23, 'Y':24, 'Z':25,
        '1':26, '2':27, '3':28,
        '4':29, '5':30, '6':31,
        '7':32, '8':33, '9':34,
        '0':35, ', ':36, '.':37,
        '?':38, '/':39, '-':40,
        '(':41, ')':42, ' ':43}
cryptage = Entry(cy, width=50, borderwidth=5)
cryptage.grid(row=0, column=0, columnspan=3, padx = 10, pady=10)    

def encrypt():
    input = cryptage.get()
    cypher = ''
    keycode = ''
    cypher_wip = ''
    space = 0
    Base = input
    BaseLength = len(Base)
    print(input)
    print(BaseLength)
    while len(keycode) < BaseLength:
        numb = round(random.randrange(0,42)/10)*10
        code_list = list(key.keys())
        key_list = list(key.values())
        position = key_list.index(numb)
        keycode += code_list[position]
        print(code_list[position])
        cypher_wip += str(ord(str(input[space])) + numb) + " "
        space += 1
    print(cypher_wip)
        
    output_1.insert(END, keycode)
    output_2.insert(END, cypher_wip)
    
button_enter = Button(cy, text="enter", command=encrypt)
button_enter.grid(row=3)

output_1 = Text(cy, width=50, borderwidth=5, height= 5)
output_2 = Text(cy, width=50, borderwidth=5, height= 5)
output_1.grid(row = 1, column=0)
output_2.grid(row= 2, column=0)
cy.mainloop()
