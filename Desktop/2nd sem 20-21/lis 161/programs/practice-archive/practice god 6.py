def grade(grd):
    if grd >= 0.9 :
        return 'Grade A'
    elif grd >= 0.8 :
        return 'Grade B'
    elif grd >= 0.7 :
        return 'Grade C'
    elif grd >= 0.6 :
        return 'Grade D'
    else :
        return 'Grade F'
try:
    grado=input("Hey! What's your grade? ",)
    grado=float(grado)
except:
    print("Please type an appropriate number",)
    exit()
else:
    if 1<grado:
        print("Please type an appropriate number",)
        exit()
    elif grado<0:
        print("Please type an appropriate number",)
        exit()
    else:
        print("Calculating",)

gred=grade(grd=grado)
print("Here's your grade:", gred)
