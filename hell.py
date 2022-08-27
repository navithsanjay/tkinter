from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)

scrollbar.pack( side = RIGHT, fill = Y )
def twet():
    T = Text(root, height = 10, width = 50)
    T.pack(padx=10,pady=20)
    root.mainloop()
b3 = Button(root, text = "example btn",
            background = "green", fg = "white",command=twet).place(x=100,y=100)

root.mainloop()