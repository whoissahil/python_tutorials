######################### Advance Parameters #########################

# can add default value of parameter --- name="Sahil" and then even if you call the function w/o values it will work
def demo(name="Sahil", verb="running", noun="Cheese"):
    print (name + " is " + verb + " with " + noun + " !")

demo("Sahil", "running", "cheese")
demo()

# can initialise here only so that the order doesn't matter
demo(verb="walking")

######################### Return #########################

def demo2(num1, num2):
    return(num1 + num2)

ans = demo2(3,6)
print(ans)

