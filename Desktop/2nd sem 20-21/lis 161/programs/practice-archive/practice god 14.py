count = 0

try:
    entrer = input("What is your file: ",)
    reader = open(entrer)

except:
    errs = entrer.find(".txt")
    errs = True
    print("File doesn't seem to exist.")
    exit()

for linya in reader:
    hati = linya.rstrip().split()
    if len(hati) == 0: continue
    if hati[0] != "From" : continue
    print(hati[1])
    count = count + 1

print("There were", count ,"lines in the file:", entrer , "with From as the first word.")
print(hati)
