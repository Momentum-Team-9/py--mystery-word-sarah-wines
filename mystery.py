# choose difficulty: easy(4-6), normal(6-8), hard(8+)
# sort words by length, select words from list within range of level
# ensure random word does not change

# ???import the random module
# ???import random


mystery_word = "kitty"
print(mystery_word)
gameboard = ["_"] * len(mystery_word)
print(gameboard)
print("Your word has " + str(len(mystery_word)) + " letters.")
guess = input("Please guess a letter, you have 8 guesses ")
print(guess)
if guess in mystery_word:
    index = mystery_word.index(guess)
    gameboard[index] = guess
    print(gameboard)
