#SetUp
import functionwget
import getpass
import Settings
import hashlib
import time
import os
md5 = hashlib.md5()
command_help ='''\
_____/[CommandHelp]\_____
Help(help)——Show Help
LogOut(logout)——LogOut
Exit(exit,quit)——Exit OS
......
—————\    [End]    /—————
'''

#RegIster
usrTrue = False
if Settings.UsrHasReged == False:
    print('Please RegIster First!')
    while Settings.UsrHasReged == False: 
        usrname = input("UserName: ")
        usrpwd = getpass.getpass()
        if usrname == "" or usrpwd == "":
            print('Please Enter Username Or Password!')
        else:
            print('RegIster Successful')
            md5.update(usrpwd.encode(encoding="utf-8"))
            usrpwd = md5.hexdigest()
            Settings.UsrHasReged = True
            Settings.users[usrname] = usrpwd
        print(usrpwd)

#LogIn
if Settings.UsrHasReged == True:
    print('Please Login First!')
    while usrTrue == False:
        usrname = input("Username: ")
        usrpwd = getpass.getpass()
        md5.update(usrpwd.encode(encoding="utf-8"))
        usrpwd = md5.hexdigest()
        if usrname == "" or usrpwd == "":
            print('Please Enter Username Or Password!')
        elif usrpwd == Settings.users[usrname]:
            print('Login Successful')
            usrTrue = True
        else:
            print('Wrong username or password!')
            usrTrue = False

#Main
while usrTrue == True:
    usrInput = input(">>>")
    if usrInput == "LogOut" or usrInput == "logout":
        usrInput = False
    elif usrInput == "Help" or usrInput == "help":
        print(command_help)
    elif usrInput == "Exit" or usrInput == "exit" or usrInput == "quit":
        print('GoodBye!')
        time.sleep(3)
        exit()
    elif usrInput == "wget":
        usrInput = input("URL:")
        functionwget.download(usrInput)
    elif usrInput == "pom":
        usrInput = input("[POM]Search:")
    else:
        print('Unkown Command,Type "Help" to show Help')