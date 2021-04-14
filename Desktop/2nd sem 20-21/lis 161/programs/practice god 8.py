#numb = int(input("Type a number:",))
#while numb>0 :
#    print(numb)
#    numb = numb - 1
#print("Blastoff!")
#print(numb)
oll = 0
cot = 0.0

while True:
    trst = input("Type a number:",)
    if trst == 'done' :
        str(trst)
        break
    try :
        ftrst = float(trst)
    except:
        print("Please type a number.",)
        exit()

    oll = oll + 1
    cot = ftrst + cot
    print(ftrst)
    continue
    if str(trst):
        str(trst)
        print("Please type a number.",)
        break

    print(trst)
print(oll, cot, cot/oll)
