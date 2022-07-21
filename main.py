import winreg

# with winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT) as hkey:
#     key =  winreg.CreateKey(key,'Directory\\Background\\shell\\new_test') 
#     winreg.CloseKey(key)

# def create_key():
#     key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT,'Directory\\Background\\shell\\new_test\\command') 
#     winreg.SetValue(key, '', winreg.REG_SZ, 'C:\Program Files\Google\Chrome\Application\chrome.exe')
#     winreg.CloseKey(key)
# create_key()

# begin
print('''
1) NETWORKING
2) FILES :
3) DEVELOPER :
4) GENERAL :
''')

fchoice = int(input("CHOOSE CATEGORY [NUMBER] : "))

content = {
    1: '''
1) COPY-IP tool
    ''',
    
    2: '''
1) Delete TMP (temp) files tool
2) Show Hidden Files
3) File - Permanently delete 
4) File - Run/Open as Admin tool
    ''',

    3: '''
1) Copy as Path
    ''',

    4: '''
1) ScreenShot tool
2) Browser (Chrome, Brave, Firefox)
3) Task Manager
4) Shutdown
5) Restart
    '''
}
print(content[fchoice])
schoice = int(input("WHAT DO YOU WANNA ADD? [NUMBER} : "))
