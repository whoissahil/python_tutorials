# l = 10            # Global
# def function1(n):
#     # l = 5         # Local
#     m = 8         # Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n , "i have printed")

# function1("this is me")


x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

harry()
print(x)