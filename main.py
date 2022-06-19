from system import functionwget
import getpass
import UserSettings

#getpassword
usrTrue = False
while usrTrue == False:
    usrname = input("Username: ")
    usrpwd = getpass.getpass()
    if usrpwd == UserSettings.usersetting[usrname]:
        usrTrue = True
    elif UserSettings.usersetting[usrname] == 0 and usrpwd == "":
        usrTrue = True
    else:
        usrTrue = False

usrInput = ""
while True:
    usrInput = input(">>>")
    if usrInput == "wget":
        usrInput = input("URL:")
        functionwget.download(usrInput)
    elif usrInput == "pom":
        usrInput = input("[POM]Search:")
        UserSettings.POMFindimport()
    else:
        pass