import random

num = random.randint(1,10)
print (num)

while True:
    try:
        guess = int(input("Please guess a number: "))
        while guess != num:
            guess = int(input("Please guess a number: "))
        print("You win")
        break

    except Exception:
        print("Please provide an int")


# Excercise

flag = 1

while 2 ** flag < 1000000000:
    flag += 1
print(flag)

print("The answer is: {} and 2^{} is {}".format(flag, flag, 2 ** flag))

