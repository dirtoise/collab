try:
    hrs = input("Enter Hours: ",)
    hrs = float(hrs)
except:
    print("Error. Bro, type a numerical value.")
    quit()

try:
    rte = input("Enter Rate: ",)
    rte = float(rte)
except:
    print("Error. Bro, type a numerical value.")
    quit()

if hrs>40 :
    pay = 40 * rte
    opay = pay + (hrs-40) * (rte*1.5)
    print("Wow. Working overtime. Here's your pay:", opay)

else :
    pay = hrs * rte
    print("Wow. A hard worker. Here's your pay:", pay)
