# choose difficulty: easy(4-6), normal(6-8), hard(8+)
# sort words by length, select words from list within range of level
# ensure random word does not change

# ???import the random module
# ???import random
import random


def mysteryword():
    with open("words.txt") as words_list:
        words = words_list.read().split()
    easy_words = []
    normal_words = []
    hard_words = []
    for word in words:
        if len(word) == 4 or len(word) == 5:
            easy_words.append(word)
        elif len(word) == 6 or len(word) == 7:
            normal_words.append(word)
        elif len(word) == 7 or len(word) == 8:
            hard_words.append(word)
    level = input("Easy, normal, or hard?")
    if level == "easy" or "Easy":
        mystery_word = random.choice(easy_words).lower()
    if level == "normal" or "Normal":
        mystery_word = random.choice(normal_words).lower()
    if level == "hard" or "Hard":
        mystery_word = random.choice(hard_words).lower()
    print(mystery_word)
    gameboard = ["_"] * len(mystery_word)
    # gameover = False
    print(" ".join(gameboard))
    print("Your word has " + str(len(mystery_word)) + " letters.")
    guess = input("Please guess a letter, you have 8 guesses ")
    print(guess)
    # while gameover is False:
    if guess in mystery_word:
        index = mystery_word.index(guess)
        gameboard[index] = guess
        print(gameboard)
    else:
        print("That letter does not appear, you have X guesses remaining, try again.")


mysteryword()
