news = []

try:
    entrer = input("What is your file: ",)
    reader = open(entrer)

except:
    errs = entrer.find(".txt")
    errs = True
    print("File doesn't seem to exist.")
    exit()



for linya in reader:
    linya = linya.split()
    for salita in linya:
        if salita != news:
            news.append(salita)
            news.sort()
print(news)

#    print(linya)
#    if len(linya) != len(set(linya)):
#        print("true")
#    else:
#        print("false")
#    linya = linya.extend(linya)



#    splitter = linya.split()
#    print(splitter)


#    splitter.sort()
#    print(linya)
