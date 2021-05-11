try:
    filename = input("What is your file: ",)
    handle = open(filename)
except:
    errs = filename.find(".txt")
    errs = False
    print("File doesn't seem to exist.")
    exit()

days = dict()
mailys = dict()
mailers = dict()
for line in handle:
    if line.startswith("From "):
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1
        mails = line.split()[1]
        mailys[mails] = mailys.get(mails, 0) + 1
        mailer = line.split()[1]
        slash = mailer.split("@")[1]
        mailers[slash] = mailers.get(slash, 0) + 1

print("Day count:", days)
print("Email count:", mailys)
print("Domain count:", mailers)


mostest = -1
mailest = None
for mx,my in mailys.items():
    if my>mostest:
        mostest = my
        mailest = mx
print("The email that appeared most:", mailest, "appearead this many times:",mostest)


#for dz,num in mails.items():
#    print(dz, num)
