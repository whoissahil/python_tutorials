shoes = ("Spizikes", "Air Force 1", "Curry 2", "Melo 5")

def appendtotuple(thetuple, value):
    newShoes = list(thetuple)
    newShoes.append(value)
    return(tuple(newShoes))

print (appendtotuple(shoes, "Sahil"))
