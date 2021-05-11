#numb = int(input("Type a number:",))
#while numb>0 :
#    print(numb)
#    numb = numb - 1
#print("Blastoff!")
#print(numb)
oll = 0
cot = 0.0
try :
    inpx = int(input("How many numbers do you want?",))
    print(inpx,"? Okay.")

except:
    print("Numbers only please.",)
    exit()

else:
    if inpx >= 10 :
        print("Are you sure?<Y/N>")
        conf = input()
        if conf == "Y" :
            print("Okay. If you say so...")
        elif conf == "N" :
            print("Good idea.")
            exit()
        else:
            print("I don't understand.")
            exit()

while inpx > 0:
    trst = input("Type a number:",)
    inpx = inpx - 1
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
