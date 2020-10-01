def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)

function_name_print("hari", "jack", "shivam", "ryan", "vibhor")

def funargs(a, *args, **kwarg):
    print(type(args))
    print(normal)
    for item in args:
        print(item)
    print("\nNow i would like to introduce some of our hero's")
    for key, value in kwarg.items():
        print(f"{key} is a {value}")

normal = "I am an normal argument and student are:"
har = ["hari", "jack", "shivam", "ryan", "vibhor"]
kw  = {"rohan":"monitor", "hari":"coder", "ryna":"cr", "vibhor":"2ic"}

funargs(normal, *har, **kw)

# We use *args and **kwargs as an argument when we have no doubt about the number of  arguments we should pass in a function.