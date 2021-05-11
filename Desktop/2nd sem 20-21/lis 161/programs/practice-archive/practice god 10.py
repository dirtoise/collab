try :
    nepo = (input("File name: ",))
    print("Trying to open", nepo,)
except :
    print("Files doesn't exist.")
    exit()
else:
    if nepo =="na na boo boo" :
        print("NA NA BOO BOO TO YOU - You have been cyberpunk'd!")
        exit()


nepon = open(nepo)
dracula = 0
for nsubj in nepon:
    if nsubj.startswith('Subject:'):
        dracula = dracula + 1
print("There were", dracula, "subject lines in", nepo,)
