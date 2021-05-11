try:
    line = input("What is your file: ",)
    handle = open(line)

except:
    errs = line.find(".txt")
    errs = False
    print("File doesn't seem to exist.")
    exit()

dito = dict()
for line in handle:
    line = line.rstrip()
#    print(line)
    splitter = line.split()
#    print(splitter)
    for splits in splitter:
        dito[splits] = dito.get(splits, 0) + 1
#            dito[splits] = dito[splits] + 1
#        else:
#            dito[splits] = 1
#        print(splits, dito[splits])
#print(dito)

largest = -1
moreword = None
for k,v in dito.items():
#    print(k,v)
    if v>largest:
        largest = v
        moreword = k
print("Frequent word:", moreword, "Amount:", largest)
