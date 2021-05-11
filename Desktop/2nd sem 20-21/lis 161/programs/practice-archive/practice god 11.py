ecin = input("What is your file: ",)
necin = open(ecin)
for brecin in necin:
    mecin = brecin.rstrip()
    print(mecin.upper())
    
