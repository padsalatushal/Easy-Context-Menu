from tkinter import *
import winreg,os,shutil


root = Tk()


root.geometry('750x400')
root.minsize(400, 300)
root.title('Easy Context Menu')

Label(root, text='Easy Context Menu', font='comicsansms 29 bold').grid(row=0, column=1)

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

# https://www.winhelponline.com/blog/copy-as-path-always-show-right-click-windows-10/
def copy_as_path():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Allfilesystemobjects\\shell\\windows.copyaspath')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Copy &as path')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'imageres.dll,-5302')
    winreg.SetValueEx(key, 'InvokeCommandOnSelection', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'VerbHandler', 0, winreg.REG_SZ,
                      '{f3d06e7c-1e45-4a26-847e-f9fcdee59be0}')
    winreg.SetValueEx(key, 'VerbName', 0, winreg.REG_SZ, 'copyaspath')
    winreg.CloseKey(key)

# https://www.winhelponline.com/blog/ribbon-command-right-click-menu-windows-10/
def delete_permanetly():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'AllFileSystemObjects\\shell\\delete_permanetly')
    winreg.SetValueEx(key, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, 'ExplorerCommandHandler', 0,
                      winreg.REG_SZ, '{E9571AB2-AD92-4ec6-8924-4E5AD33790F5}')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'shell32.dll,-240')
    winreg.CloseKey(key)



# https://www.winhelponline.com/blog/add-select-all-option-to-the-context-menu-in-windows-vista/
def select_all():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Directory\\Background\\shell\\Windows.selectall')

    winreg.SetValue(key, 'command', winreg.REG_SZ, '')

    key1 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                            'Directory\\Background\\shell\\Windows.selectall\\command')
    winreg.SetValueEx(key1, 'DelegateExecute', 0, winreg.REG_SZ,
                      '{aa28fbc7-59f1-4c42-9fd8-ba2be27ea319}')

    winreg.SetValueEx(key, 'CanonicalName', 0, winreg.REG_SZ,
                      '{b33bf5af-76d5-4d10-93e7-d8e22e93798f}')
    winreg.SetValueEx(key, 'CommandStateHandler', 0,
                      winreg.REG_SZ, '{3756e7f5-e514-4776-a32b-eb24bc1efe7a}')
    winreg.SetValueEx(key, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, 'Description', 0,
                      winreg.REG_SZ, '@shell32.dll,-31277')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'imageres.dll,-5308')
    winreg.SetValueEx(key, 'ImpliedSelectionModel', 0, winreg.REG_DWORD, 32)
    winreg.SetValueEx(key, 'MUIVerb', 0, winreg.REG_SZ, '@shell32.dll,-31276')
    winreg.SetValueEx(key, 'NeverDefault', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, 'Position', 0, winreg.REG_SZ, 'Bottom')

    winreg.CloseKey(key)
    winreg.CloseKey(key1)



# https://helpdeskgeek.com/how-to/add-shutdown-and-restart-to-the-right-click-context-menu-in-windows-8/

def shutdown():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Directory\\Background\\shell\\Shutdown')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'shutdown -s -t 00 -f')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'shell32.dll,-221')
    winreg.SetValueEx(key, 'Position', 0, winreg.REG_SZ, 'Bottom')
    winreg.CloseKey(key)


# https://superuser.com/questions/1151844/how-to-toggle-show-hide-hidden-files-in-windows-through-command-line

def show_hidden_files_toggle():
    key1 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                            'Folder\\shell\\Windows.ShowHiddenFiles')
    key2 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                            'Directory\\Background\\shell\\Windows.ShowHiddenFiles')

    winreg.SetValueEx(key1, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key1, 'Description', 0,
                      winreg.REG_SZ, '@shell32.dll,-37573')
    winreg.SetValueEx(key1, 'ExplorerCommandHandler', 0,
                      winreg.REG_SZ, '{f7300245-1f4b-41ba-8948-6fd392064494}')
    winreg.SetValueEx(key1, 'MUIVerb', 0, winreg.REG_SZ, '@shell32.dll,-37572')

    winreg.SetValueEx(key2, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key2, 'Description', 0,
                      winreg.REG_SZ, '@shell32.dll,-37573')
    winreg.SetValueEx(key2, 'ExplorerCommandHandler', 0,
                      winreg.REG_SZ, '{f7300245-1f4b-41ba-8948-6fd392064494}')
    winreg.SetValueEx(key2, 'MUIVerb', 0, winreg.REG_SZ, '@shell32.dll,-37572')

    winreg.CloseKey(key1)
    winreg.CloseKey(key2)


def delete_tmp_file():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Directory\\Background\\shell\\delete_tmp_file')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Clean Temporary Files')
    winreg.SetValue(key, 'command', winreg.REG_SZ,
                    'cmd.exe /C del /q/f/s %temp%\*')
    winreg.CloseKey(key)


def snipping_tool():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,
                           'Directory\\Background\\shell\\snipping_tool')
    winreg.SetValue(key, 'command', winreg.REG_SZ,
                    'C:\Windows\system32\SnippingTool.exe')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Snipping Tool')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ,
                      'C:\Windows\system32\SnippingTool.exe')
    winreg.CloseKey(key)


def screenshot():
    #move screenshot.exe from current folder to system32 folder
    src_path = os.getcwd()+'\screenshot.exe'
    dst_path = r'C:\Windows\System32\screenshot.exe'
    shutil.copy(src_path, dst_path)

    # creating key for screenshot
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\screenshot')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Screenshot')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'C:\Windows\System32\screenshot.exe' )
    winreg.CloseKey(key)

    # making folder in desktop for saving screenshot

    # For getting desktop path
    Desktoppath = os.path.join((os.environ['USERPROFILE']),'Desktop')
    sspath = os.path.join(Desktoppath,'Screenshot')
    
    if os.path.isdir(sspath) == True:
        # print("ssfolder  exists")
        pass
    else:
        os.mkdir(sspath)
        # print("ssfolder created")

    # changing defalut location for saving screenshot
    # https://answers.microsoft.com/en-us/windows/forum/all/restore-screenshot-locations/1c410319-aacf-4c94-9d70-428b9a30d21d

    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders', 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}', 0, winreg.REG_SZ, sspath)
    winreg.CloseKey(key)
   
    #restart explorer.exe
    os.system('taskkill /F /IM explorer.exe & start explorer')




chrome_check_var = IntVar()
task_manager_check_var = IntVar()
copy_as_path_check_var = IntVar()
delete_permanetly_check_var = IntVar()
select_all_check_var = IntVar()
shutdown_check_var = IntVar()
show_hidden_files_toggle_check_var = IntVar()
delete_tmp_file_check_var = IntVar()
snipping_tool_check_var = IntVar()
screenshot_check_var = IntVar()


def var_state():
    print("chrome : ",chrome_check_var.get())
    print("Task Manager : ",task_manager_check_var.get())
    print("Copy As Path: ",copy_as_path_check_var.get())
    print("Delete permanetly :", delete_permanetly_check_var.get())
    print("Select All :", select_all_check_var.get())
    print("Shutdown :",shutdown_check_var.get())
    print("Show Hidden items toggle :", show_hidden_files_toggle_check_var.get())
    print("Delete tmp file:", delete_tmp_file_check_var.get())
    print("Snipping tool :", snipping_tool_check_var.get())
    print("Screenshot :", screenshot_check_var.get())

def apply():
    if chrome_check_var.get()==1:
        Chrome()
    if task_manager_check_var.get()==1:
        task_manager()
    if copy_as_path_check_var.get()==1:
        copy_as_path()
    if delete_permanetly_check_var.get()==1:
        delete_permanetly()
    if select_all_check_var.get()==1:
        select_all()
    if shutdown_check_var.get()==1:
        shutdown()
    if show_hidden_files_toggle_check_var.get()==1:
        show_hidden_files_toggle()
    if delete_tmp_file_check_var.get()==1:
        delete_tmp_file()
    if snipping_tool_check_var.get()==1:
        snipping_tool()
    if screenshot_check_var.get()==1:
        screenshot()

Checkbutton(root, text='Chrome', font='18', variable=chrome_check_var).grid(row=1, column=0)
Checkbutton(root, text='Task Manager', font='18', variable=task_manager_check_var).grid(row=2, column=0)
Checkbutton(root, text='Copy As Path', font='18', variable=copy_as_path_check_var).grid(row=3, column=0)
Checkbutton(root, text='Delete Permanetly', font='18', variable=delete_permanetly_check_var).grid(row=1, column=1)
Checkbutton(root, text='Select All', font='18', variable=select_all_check_var).grid(row=2, column=1)
Checkbutton(root, text='Shutdown', font='18', variable=shutdown_check_var).grid(row=1, column=2)
Checkbutton(root, text='Show hidden item toggle', font='18', variable=show_hidden_files_toggle_check_var).grid(row=2, column=2)
Checkbutton(root, text='Delete Temporary files', font='18', variable=delete_tmp_file_check_var).grid(row=3, column=2)
Checkbutton(root, text='Snipping tool', font='18', variable=snipping_tool_check_var).grid(row=4, column=0)
Checkbutton(root, text='Screenshot', font='18', variable=screenshot_check_var).grid(row=5, column=0)




Button(root, text='show', command=var_state).grid(row=6, sticky=W, column=0)
Button(root, text='Apply', command=apply).grid(row=6, sticky=W, column=1)


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
chrome_path = 'Directory\\Background\\shell\\Chrome'
task_manager_path = 'Directory\\Background\\shell\\task_manager'
copy_as_path_path = 'Allfilesystemobjects\\shell\\windows.copyaspath'
delete_permanetly_path = 'AllFileSystemObjects\\shell\\delete_permanetly'
select_all_path = 'Directory\\Background\\shell\\Windows.selectall'
shutdown_path = 'Directory\\Background\\shell\\Shutdown'
show_hidden_files_toggle_path = 'Folder\\shell\\Windows.ShowHiddenFiles'
show_hidden_files_toggle_path1 = 'Directory\\Background\\shell\\Windows.ShowHiddenFiles'
delete_tmp_file_path = 'Directory\\Background\\shell\\delete_tmp_file'
snipping_tool_path = 'Directory\\Background\\shell\\snipping_tool'
screenshot_path = 'Directory\\Background\\shell\\screenshot'

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
    if copy_as_path_check_var.get()==1:
        keys.append(copy_as_path_path)
    if delete_permanetly_check_var.get()==1:
        keys.append(delete_permanetly_path)
    if select_all_check_var.get()==1:
        keys.append(select_all_path)
    if shutdown_check_var.get()==1:
        keys.append(shutdown_path)
    if show_hidden_files_toggle_check_var.get()==1:
        keys.append(show_hidden_files_toggle_path)
        keys.append(show_hidden_files_toggle_path1)
    if delete_tmp_file_check_var.get()==1:
        keys.append(delete_tmp_file_path)
    if snipping_tool_check_var.get()==1:
        keys.append(snipping_tool_path)
    if screenshot_check_var.get()==1:
        keys.append(screenshot_path)


    delete_key()



Button(root, text='remove', command=remove).grid(row=6, sticky=W, column=2)

root.mainloop()
