

try:
    line = input("What is your file: ",)
    handle = open(line)

except:
    errs = line.find(".txt")
    errs = True
    print("File doesn't seem to exist.")
    exit()

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print("Counts:", counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)
