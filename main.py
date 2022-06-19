from system import functionwget
import getpass
import UserSettings

#getpassword


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