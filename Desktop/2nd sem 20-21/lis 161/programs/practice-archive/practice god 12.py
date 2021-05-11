def chop(list):
    list.pop(0)
    list.pop(-1)
    return

def middle(list):
    newnew = list.copy()
    newnew.pop(0)
    newnew.pop(-1)
    return newnew

list = ["dragon", "wizard", "magic", "fate"]

print(middle(list))
print(list)
