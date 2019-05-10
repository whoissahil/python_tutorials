# Lists

# Spizikes
# Air Force 1
# Curry 2
# Melo 5

shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5", 3, 4.5, True]
print(shoes)
print (shoes[0], shoes[1])
print(shoes[-1])
print (type(shoes))

shoes.append("Demo") #append
print(shoes)
shoes.insert(2, "Demo") #insert
print(shoes)
shoes[2] = "Demo2" #update
print(shoes)
del(shoes[8]) #del
shoes.remove("Demo2") #del
print(shoes)
print (len(shoes)) #length

