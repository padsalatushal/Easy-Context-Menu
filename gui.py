from tkinter import *
import winreg

root = Tk()

root.geometry('500x400')
root.minsize(400, 300)
root.title('Easy Context Menu')


Label(root, text='Easy Context Menu', font='comicsansms 29 bold').grid(row=0, column=2)

def Chrome():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Directory\\Background\\shell\\Chrome')
    winreg.SetValue(key, 'command', winreg.REG_SZ,
                    'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ,
                      'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.CloseKey(key)


def var_state():
    print(var1.get())
var1 = IntVar()

def apply():
    if var1.get()==1:
        Chrome()
        print('Done')
    elif var1.get()==0:
        print('noting happen')
    



Checkbutton(root, text='chrome', font='18', variable=var1).grid(row=1, column=0)
Button(root, text='show', command=var_state).grid(row=2, sticky=W, column=2)
Button(root, text='Apply', command=apply).grid(row=2, sticky=W, column=1)

root.mainloop()
