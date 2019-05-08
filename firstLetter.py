def firstLetter(word):
    print ("The first letter of the word you gave is: {}".format(word[0]))

while True:
    try:
        word_input = input("Please enter the word: ")
        firstLetter(word_input)
        break
    except Exception:
        print ("Please enter correctly!")
