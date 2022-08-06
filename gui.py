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

def task_manager():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\task_manager')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'C:\Windows\system32\Taskmgr.exe')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Task Manager')
    winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ, 'C:\Windows\system32\Taskmgr.exe')
    winreg.CloseKey(key)

chrome_check_var = IntVar()
task_manager_check_var = IntVar()

def var_state():
    print("chrome : ",chrome_check_var.get())
    print("Task Manager : ",task_manager_check_var.get())

def apply():
    if chrome_check_var.get()==1:
        Chrome()
    if task_manager_check_var.get()==1:
        task_manager()

Checkbutton(root, text='Chrome', font='18', variable=chrome_check_var).grid(row=1, column=0)
Checkbutton(root, text='Task Manager', font='18', variable=task_manager_check_var).grid(row=2, column=0)

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
            # print("Removed %s\\%s " % (current_key, sub_key))
        except OSError:
            delete_sub_key(key0, "\\".join([current_key, sub_key]))
            # No extra delete here since each call
            # to delete_sub_key will try to delete itself when its empty.

    winreg.DeleteKey(open_key, "")
    open_key.Close()
    # print("Removed %s" % current_key)
    return


# List of keys to delete
chrome_path = 'Directory\Background\shell\Chrome'
task_manager_path = 'Directory\\Background\\shell\\task_manager'
keys = []

def delete_key():
    for key in keys:
        try:
            delete_sub_key(winreg.HKEY_CLASSES_ROOT, key)
        except OSError as e:
            print(e)

def remove():
    if chrome_check_var.get()==1:
        keys.append(chrome_path)
    if task_manager_check_var.get()==1:
        keys.append(task_manager_path)    
    delete_key()


Button(root, text='remove', command=remove).grid(row=3, sticky=W, column=2)

root.mainloop()
