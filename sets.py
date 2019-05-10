shoes = set(["Spizikes", "Air Force 1", "Curry 2", "Melo 5"])

# sets has no particular order
print (shoes)

#add a value to set
shoes.add("Demo")
print(shoes)

#delete a value
shoes.remove("Curry 2") #this might give error if missplelled so better use .discard which does the same but ignores if not spelled right
print(shoes)


# Project Sets

numbers = set([3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2])
print (numbers)
#sets doesnt return one value twice

