import tkinter as tki

a=tki.Tk()
a.geometry('500x400')
a.title('REMAINDER')
#a.configure(bg='')

option=['Whatsapp Remaider','Voice Remainder','System Auto Shutdown','Auto File Opening']
values=tki.StringVar(a)
values.set('Type of Remainder')
menu=tki.OptionMenu(a,values,*option)
menu.pack()

def answer():
    print('Seleted Option:{}'.format(values.get()))
    return None

button=tki.Button(a,text='submit',command=answer)
button.pack()

menubar=tki.Menu(a)


file=tki.Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New File',command=None)
file.add_command(label='Open',command=None)
file.add_command(label='Save',command=None)
file.add_separator()
file.add_command(label='Exit',command=None)


edit=tki.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Edit',command=None)
edit.add_command(label='Cut',command=None)
edit.add_command(label='Copy',command=None)
edit.add_command(label='Paste',command=None)
edit.add_command(label='Select all',command=None)
edit.add_separator()
edit.add_command(label='Find...',command=None)
edit.add_command(label='Find again',command=None)

help=tki.Menu(menu,tearoff=0)
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='Help',command=None)
help.add_command(label='Remainder Help',command=None)
help.add_command(label='Demo',command=None)
help.add_separator()
help.add_command(label='About Remaider',command=None)

a.configure(menu=menubar)
a.mainloop()