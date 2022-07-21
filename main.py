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