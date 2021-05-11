filename = input("Enter a file name: ")
fhand = open(filename, 'r')
days = {}
mailers = {}
for line in fhand:
    if line.startswith("From "):
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1
        mailer = line.split()[1]
        slash = mailer.split("@")[1]
        mailers[slash] = mailers.get(slash, 0) + 1

print(mailers)
print(days)
