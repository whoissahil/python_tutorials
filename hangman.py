lives = 2
word = "Apple"
wordList = list(word.lower())
# print(wordList)

def checkLives(bool):
    global lives
    if True:
        # return lives
        print(lives)
    if False:
        lives -= 1
        # return lives
        print(lives)


def check(alp):
    global wordList
    global lives

    if len(wordList) != 0:
        if alp in wordList:
            print("YES")
            # checkLives(True)
            wordList.remove(alp)  # del
            # print(len(wordList))
        else:
            print("NO")
            # print(len(wordList))
            # checkLives(False)
            lives -= 1
    else:
        print("You Won")


while True:
    try:
        alp = input("Please guess an alphabet: ")
        check(alp)
        if lives == 0:
            break
    except Exception:
        print("Only Alphabet")



    
