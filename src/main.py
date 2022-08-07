import winreg
import os,shutil
'''
# basic way to add key in registry
with winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT) as hkey: #get the neceessary hkey
    key =  winreg.CreateKey(hkey,'Directory\\Background\\shell\\new_test') 
    winreg.CloseKey(key)

# Add key in registry Using function
def create_key():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,'Directory\\Background\\shell\\Chrome\\command') 
    winreg.SetValue(key, '', winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.CloseKey(key)
create_key()

# for adding icon 
key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT,'Directory\\Background\\shell\\Chrome\\', 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
winreg.CloseKey(key)

# Delete key
key = 'Directory\\Background\\shell\\Chrome\\command'
winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT,key)

'''

def Chrome():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,'Directory\\Background\\shell\\Chrome') 
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.CloseKey(key)
Chrome()

def task_manager():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\task_manager')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'C:\Windows\system32\Taskmgr.exe')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Task Manager')
    winreg.SetValueEx(key, 'icon', 0, winreg.REG_SZ, 'C:\Windows\system32\Taskmgr.exe')
    winreg.CloseKey(key)
task_manager()

#https://www.winhelponline.com/blog/copy-as-path-always-show-right-click-windows-10/

def copy_as_path():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Allfilesystemobjects\\shell\\windows.copyaspath')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Copy &as path')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'imageres.dll,-5302')
    winreg.SetValueEx(key, 'InvokeCommandOnSelection', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'VerbHandler', 0, winreg.REG_SZ, '{f3d06e7c-1e45-4a26-847e-f9fcdee59be0}')
    winreg.SetValueEx(key, 'VerbName', 0, winreg.REG_SZ, 'copyaspath')
    winreg.CloseKey(key)

copy_as_path()

#https://www.winhelponline.com/blog/ribbon-command-right-click-menu-windows-10/
def delete_permanetly():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'AllFileSystemObjects\\shell\\delete_permanetly')
    winreg.SetValueEx(key, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, 'ExplorerCommandHandler', 0, winreg.REG_SZ, '{E9571AB2-AD92-4ec6-8924-4E5AD33790F5}')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'shell32.dll,-240')
    winreg.CloseKey(key)
delete_permanetly()


#https://www.winhelponline.com/blog/add-select-all-option-to-the-context-menu-in-windows-vista/
def select_all():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\Windows.selectall')

    winreg.SetValue(key, 'command', winreg.REG_SZ, '')

    key1 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\Windows.selectall\\command')
    winreg.SetValueEx(key1, 'DelegateExecute', 0, winreg.REG_SZ, '{aa28fbc7-59f1-4c42-9fd8-ba2be27ea319}')
    
    winreg.SetValueEx(key, 'CanonicalName', 0, winreg.REG_SZ, '{b33bf5af-76d5-4d10-93e7-d8e22e93798f}')
    winreg.SetValueEx(key, 'CommandStateHandler', 0, winreg.REG_SZ, '{3756e7f5-e514-4776-a32b-eb24bc1efe7a}')
    winreg.SetValueEx(key, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, 'Description', 0, winreg.REG_SZ, '@shell32.dll,-31277')
    winreg.SetValueEx(key,'Icon' ,0, winreg.REG_SZ, 'imageres.dll,-5308')
    winreg.SetValueEx(key,'ImpliedSelectionModel' ,0, winreg.REG_DWORD, 32)
    winreg.SetValueEx(key,'MUIVerb' ,0, winreg.REG_SZ, '@shell32.dll,-31276')
    winreg.SetValueEx(key,'NeverDefault' ,0, winreg.REG_SZ, '')
    winreg.SetValueEx(key,'Position' ,0, winreg.REG_SZ, 'Bottom')

    winreg.CloseKey(key)
    winreg.CloseKey(key1)
select_all()


# https://helpdeskgeek.com/how-to/add-shutdown-and-restart-to-the-right-click-context-menu-in-windows-8/
def shutdown():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\Shutdown')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'shutdown -s -t 00 -f')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'shell32.dll,-221')
    winreg.SetValueEx(key,'Position' ,0, winreg.REG_SZ, 'Bottom')
    winreg.CloseKey(key)
shutdown()


# https://superuser.com/questions/1151844/how-to-toggle-show-hide-hidden-files-in-windows-through-command-line
def show_hidden_files_toggle():
    key1 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Folder\\shell\\Windows.ShowHiddenFiles')
    key2 = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\Windows.ShowHiddenFiles')

    winreg.SetValueEx(key1, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key1, 'Description', 0, winreg.REG_SZ, '@shell32.dll,-37573')
    winreg.SetValueEx(key1, 'ExplorerCommandHandler', 0, winreg.REG_SZ, '{f7300245-1f4b-41ba-8948-6fd392064494}')
    winreg.SetValueEx(key1, 'MUIVerb', 0, winreg.REG_SZ, '@shell32.dll,-37572')

    winreg.SetValueEx(key2, 'CommandStateSync', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key2, 'Description', 0, winreg.REG_SZ, '@shell32.dll,-37573')
    winreg.SetValueEx(key2, 'ExplorerCommandHandler', 0, winreg.REG_SZ, '{f7300245-1f4b-41ba-8948-6fd392064494}')
    winreg.SetValueEx(key2, 'MUIVerb', 0, winreg.REG_SZ, '@shell32.dll,-37572')

    winreg.CloseKey(key1)
    winreg.CloseKey(key2)

show_hidden_files_toggle()


def delete_tmp_file():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\delete_tmp_file')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Clean Temporary Files')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'cmd.exe /C del /q/f/s %temp%\*') 
    winreg.CloseKey(key)

delete_tmp_file()


def snipping_tool():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'Directory\\Background\\shell\\snipping_tool')
    winreg.SetValue(key, 'command', winreg.REG_SZ, 'C:\Windows\system32\SnippingTool.exe')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'Snipping Tool')
    winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, 'C:\Windows\system32\SnippingTool.exe' )
    winreg.CloseKey(key)


snipping_tool()


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


screenshot()




def delete_sub_key(key0, current_key, arch_key=0):

    open_key = winreg.OpenKey(key0, current_key, 0,
                              winreg.KEY_ALL_ACCESS | arch_key)
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
            delete_sub_key(key0, "\\".join([current_key, sub_key]), arch_key)
            # No extra delete here since each call
            # to delete_sub_key will try to delete itself when its empty.

    winreg.DeleteKey(open_key, "")
    open_key.Close()
    print("Removed %s" % current_key)
    return


# Allows to specify if operating in redirected 32 bit mode or 64 bit, set arch_keys to 0 to disable
arch_keys = [winreg.KEY_WOW64_32KEY, winreg.KEY_WOW64_64KEY]

# Base key
root = winreg.HKEY_CLASSES_ROOT

# List of keys to delete
keys = ['Directory\Background\shell\Chrome']
'''
for key in keys:
    for arch_key in arch_keys:
        try:
            delete_sub_key(root, key, arch_key)
        except OSError as e:
            print(e)
'''



