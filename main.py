#SetUp
import getpass
import Settings
import hashlib
import time
import os
import langs
md5 = hashlib.md5()
usrTrue = False

'''
#RegIster
if Settings.UsrHasReged == False:
    print(langs.langs[Settings.lang+'-reg'])
    while Settings.UsrHasReged == False: 
        usrname = input(langs.langs[Settings.lang+'-reg-username'])
        usrpwd = getpass.getpass()
        if usrname == '' or usrpwd == '':
            print(langs.langs[Settings.lang+'-reg-noinfo'])
        else:
            print(langs.langs[Settings.lang+'-reg-success'])
            md5.update(usrpwd.encode(encoding='utf-8'))
            usrpwd = md5.hexdigest()
            Settings.UsrHasReged = True
            Settings.users[usrname] = usrpwd

#LogIn
if Settings.UsrHasReged == True:
    print(langs.langs[Settings.lang+'-login'])
    while usrTrue == False:
        usrname = input(langs.langs[Settings.lang+'-login-username'])
        usrpwd = getpass.getpass()
        md5.update(usrpwd.encode(encoding='utf-8'))
        usrpwd = md5.hexdigest()
        if usrname == '' or usrpwd == '':
            print(langs.langs[Settings.lang+'-login-noinfo'])
        elif usrpwd == Settings.users[usrname]:
            print(langs.langs[Settings.lang+'-login-success'])
            usrTrue = True
        else:
            print(langs.langs[Settings.lang+'-login-wronginfo'])
            usrTrue = False
'''

#Main
while usrTrue == True:
    usrInput = input('>>>')
    if usrInput == 'LogOut' or usrInput == 'logout':
        print(langs.langs[Settings.lang+'-logout'])
        usrInput = False
    elif usrInput == 'Help' or usrInput == 'help':
        print(langs.langs[Settings.lang+'-command-help'])
    elif usrInput == 'Lang zh_cn' or usrInput == 'lang zh_cn':
        Settings.lang = 'zh_cn'
    elif usrInput == 'Lang en_us' or usrInput == 'lang ':
        Settings.lang = 'en_us'
    elif usrInput == 'Exit' or usrInput == 'exit' or usrInput == 'quit':
        print(langs.langs[Settings.lang+'-exit'])
        time.sleep(3)
        exit()
    else:
        print(langs.langs[Settings.lang+'-command-unkown'])