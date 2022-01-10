#library
from tkinter import *

#start
mrs = Tk()
mrs.title("morse translator")

#morse translator
user = Entry(mrs, width=35, borderwidth=5)
user.grid(row=0, column=0, columnspan=3, padx = 10, pady=10)

#the part that I'm going to hate aka telling it how to translate
mrsalfa = dict([
    ("A",".-"),("B","-..."),("C_","-.-."),("D_","-.."),("E_","."),("F_","..-."),("G_","--."),("H_","...."),("I_",".."),("J_",".---"),
    ("K_","-.-"),("L_",".-.."),("M_","--"),("N_","-."),("O_","---"),("P_",".--."),("Q_","--.-"),("R_",".-."),("S_","..."),("T_","-"),
    ("U_","..-"),("V_","...-"),("W_",".--"),("X_","-..-"),("Y_","-.--"),("Z_","--..")
])
def getmrs():
    letter = user.get()
    print(type(letter))
    letter = letter.split("_")
    print (letter)
    #letter = list(letter)
    letters = " "
    letternum = 0
    for i in range(len(letter)):
        letter = letter[0][0]
        letternum = letternum + 1
        #print (letter)
        #letter = tuple(letter)
        #print (letter)
        letters =  letters + mrsalfa[letter]
        #letters = mrsalfa[letter]
        print (letters)



    T.insert(END, letters)


#def Morewords(x,y,z,d):
    #global letter1
    #global letter2
    #global letter3
    #global letters
    #global letter
    #letter = user.get()
    #test = letter.index()
    #print(test)
    #letters = mrsalfa[letter]

button_enter = Button(mrs, text="enter", command=getmrs)
button_enter.grid(row=3)

T = Text(mrs, height=1, width=25)
T.grid(row=2, column=0)
newinput = 0
letter = 0
    


#end code
mrs.mainloop()