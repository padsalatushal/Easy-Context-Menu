import winreg

with winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT) as hkey:
    key =  winreg.CreateKey(hkey,'Directory\\Background\\shell\\new_test') 
    winreg.CloseKey(key)
