import winreg

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
# delete_permanetly()

