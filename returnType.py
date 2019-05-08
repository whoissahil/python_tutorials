# # Create a function called printtype that takes one parameter. If the parameter is a string, return "String"
# # If the parameter is an int, return "Int"
# # If the parameter is a float, return "Float"

def whatIsThis(x):
    try:
        if "." in user_input:
            float(user_input)
            return("Float")
        else:
            int(user_input)
            return("Integer")
    except ValueError:
        return("String")

user_input = input("Please enter something: ")
print("What you have entered is: ", whatIsThis(user_input))
