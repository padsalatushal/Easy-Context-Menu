import winreg

# with winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT) as hkey:
#     key =  winreg.CreateKey(hkey,'Directory\\Background\\shell\\new_test') 
#     winreg.CloseKey(key)

def create_key():
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,'Directory\\Background\\shell\\new_test\\command') 
    winreg.SetValue(key, '', winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
    winreg.CloseKey(key)
create_key()
