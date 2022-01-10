#tkinter
from tkinter import *
tri = Tk()
tri.title("program de tri")
#files
dossier = [
    ['zebi', 35, '08/12/1989'],
    ['RIIIIIII', 9, '26/07/2017'],
    ['REDACTED', 69, '20/05/2020'],
]
#def to sort
def button_de_tri(test):
    test += 1
    if(test == 1):
        output_1.delete('1.0',END)
        sorted_files = sorted(dossier, key = lambda dossier: dossier[0])
        output_1.insert(END, sorted_files)
        print(test)
    elif(test == 2):
        output_1.delete('1.0',END)
        sorted_files = sorted(dossier, key = lambda dossier: dossier[1])
        output_1.insert(END, sorted_files)
        print(test)
    elif(test == 3):
        output_1.delete('1.0',END)
        sorted_files = sorted(dossier, key = lambda dossier: dossier[2])
        output_1.insert(END, sorted_files)
        print(test)
    elif(test > 3):
        sort = 1
def test1():
    global test
    test = 0
    button_de_tri(test)
#show result
output_1 = Text(tri, width=50, borderwidth=5, height= 5)
output_1.grid(row =0, column=1)
#switch
button_tri = Button(tri, text="sort files", padx=40, pady=20, command=test1, background= "#4a7a8c")
button_tri.grid(row=0, column=0)


tri.mainloop()