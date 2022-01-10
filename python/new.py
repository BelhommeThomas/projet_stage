from tkinter import *
root = Tk()

root.title('banana')
label1 = Label(root, text="hello")
user = Entry(root, width=50, font=("helvertica", 24))
user.pack()
user.insert(0, "Ecris ton Nom: ")

def sup():
    hello = "Sup " + user.get()
    myLabel = Label(root, text=hello)
    user.delete(0, "end")
    myLabel.pack()

def hello():
    hello = "Sortie " + user.get()
    myLabel = Label(root, text=hello)
    user.delete(0,"end")
    myLabel.pack()

MonButton = Button(root, text="enter", command = sup)
MonButton2 = Button(root, text="enter2", command=hello)
MonButton.pack()
MonButton2.pack()

root.mainloop()