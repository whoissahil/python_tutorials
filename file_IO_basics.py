# file IO basics:-
"""
"r" - open file for reading (default)
"w" - open file for writing(in this mode existing content of file will be deleted before writing new content)
"x" - creates file if not exists
"a" - add more content to a file(keep existing content and add new content)
"t" - text mode (default)
"b" - binary mode
"+" - read and write
"""
# open, read and readline:-

# f = open("file_IO_basics.txt")
# f = open("file_IO_basics.txt", "rt")
# f = open("file_IO_basics.txt", "rb")

# content = f.read()
# print(content)

# content = f.read(6)
# print(content)

# content = f.read(8)
# print(content)

# for line in f:
#     print(line, end="")

# content = f.readline()
# print(content)
# content = f.readline()
# print(content)
# content = f.readline()
# print(content)

# content = f.readlines()       # readlines will function returns a list of file content
# print(content)

# f.close()

# writing and appending to a file:-

# f = open("file_IO_basics2.txt", "w")
# f.write("hari is a python programer\n")
# f.close

# f = open("file_IO_basics.txt", "a")
# a = f.write("hari is a python programer.\n")
# print(a)
# f.close

# handle read and write both:-

# f = open("file_IO_basics.txt", "r+")
# print(f.read())
# f.write("thank you\n")
# f.close()

# seek and tell functions:-

f = open("file_IO_basics.txt")
print(f.tell())                             # to check file pointer current position
print(f.readline())
f.seek(0)                                   # to change file pointer position
print(f.tell())
print(f.readline())
f.seek(10)
print(f.tell())
print(f.readline())
f.close()

# using with block to open files in python:-
# if we open a file using with block then closing file is not nessasary

with open("file_IO_basics.txt") as f:
    print(f.read())
