# STRINGS


print ("Hello World!")
print ('Hello World!\n')

# Doesn't matter if single quotes or double quotes

#Python 3 supports Unicode. Meaning -

name = "Sahil🤮\n"
print (name)

#Multi Line comment

'''This is 
multi
line'''

#But the twist is if we initialise it as a string it becomes a string

demo = '''This is 
multi
line\n'''
print(demo)


# to ignore ' and " in prints put \ before them - called Escapping 

print('this\'s cool')
print("this is \"cool\"")

# concat

a = "Hello "
b = "Sahil "
print (a + b)

# to put values,

a = 1
b =2

print("a is {} and b is {}".format(a,b))

#some string functions
a = "Sahil is my name"

print(a.upper())
print(a.lower())
print(a.replace("name", "game"))

#slicing

print(a[1:4])
print(a[1:-4])

#if statement 

# boolean 

a = True

if a:
	print ("it's True")


# if elif else

a = 1830

if 2000 <= a <= 2100:
	print("Welcome 21st")
else:
	print("Old")


#example of and and or

age = 14
height = 65

if age >= 18 or height > 60:
	print ("Yes")
else:
	print ("Sorry") 

