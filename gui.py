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




def delete_sub_key(key0, current_key):

    open_key = winreg.OpenKey(key0, current_key, 0,
                              winreg.KEY_ALL_ACCESS)
    info_key = winreg.QueryInfoKey(open_key)
    for x in range(0, info_key[0]):
        # NOTE:: This code is to delete the key and all sub_keys.
        # If you just want to walk through them, then
        # you should pass x to EnumKey. sub_key = winreg.EnumKey(open_key, x)
        # Deleting the sub_key will change the sub_key count used by EnumKey.
        # We must always pass 0 to EnumKey so we
        # always get back the new first sub_key.
        sub_key = winreg.EnumKey(open_key, 0)
        try:
            winreg.DeleteKey(open_key, sub_key)
            print("Removed %s\\%s " % (current_key, sub_key))
        except OSError:
            delete_sub_key(key0, "\\".join([current_key, sub_key]))
            # No extra delete here since each call
            # to delete_sub_key will try to delete itself when its empty.

    winreg.DeleteKey(open_key, "")
    open_key.Close()
    print("Removed %s" % current_key)
    return



# List of keys to delete
chrome_path = 'Directory\Background\shell\Chrome'
keys = []

def delete_key():
    for key in keys:
        try:
            delete_sub_key(winreg.HKEY_CLASSES_ROOT, key)
        except OSError as e:
            print(e)

def remove():
    if var1.get()==1:
        keys.append(chrome_path)
        print(keys)
        delete_key()
        print("Delete Done")

Button(root, text='remove', command=remove).grid(row=3, sticky=W, column=2)

root.mainloop()
