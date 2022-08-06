from tkinter import *
import winreg

root = Tk()

root.geometry('500x400')
root.minsize(400, 300)
root.title('Easy Context Menu')


Label(root, text='Easy Context Menu', font='comicsansms 29 bold').grid(row=0, column=2)

def var_state():
    print(var1.get())


var1 = IntVar()
Checkbutton(root, text='chrome', font='18', variable=var1).grid(row=1, column=0)
Button(root, text='show', command=var_state).grid(row=2, sticky=W, column=2)


root.mainloop()
