def systemwget(inputs) :
    from system import functionwget
    def helps():
        print(
            """
Wget help:
    help       Show command list.
    download       Download a single file.
    filename       Show file name.
    exit        Exit program.
            """
        )
    def download(url):
        functionwget.download(url)
    def showfilename(url):
        functionwget.filename_from_url(url)
    Ing = True
    while Ing == True:
        if inputs == "help":
            helps()
        elif inputs == "download":
            wgetInputs = input("[Wget] Url:")
            download(wgetInputs)
        elif inputs == "filename":
            wgetInputs = input("[Wget] Url:")
            showfilename(wgetInputs)
        elif inputs == "exit":
            Ing = False
