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
        if len(word) >= 4 and len(word) < 6:
            easy_words.append(word)
        elif len(word) >= 6 and len(word) < 8:
            normal_words.append(word)
        elif len(word) >= 8:
            hard_words.append(word)
    level = input("Easy, normal, or hard? ")
    if level == "easy":
        mystery_word = random.choice(easy_words).lower()
    elif level == "normal":
        mystery_word = random.choice(normal_words).lower()
    elif level == "hard":
        mystery_word = random.choice(hard_words).lower()
    gameboard = ["_"] * len(mystery_word)
    # gameover = False
    guess_another = "yes"
    guess_count = 0
    wrong_guesses = []
    while guess_another == "yes":
        print(" ".join(gameboard))
        print("Your word has " + str(len(mystery_word)) + " letters.")
        guess = input("Please guess a letter ")
        # print(guess)
        # while gameover is False:
        if guess in mystery_word:
            index = mystery_word.index(guess)
            gameboard[index] = guess
            # print(" ".join(gameboard))
        else:
            if guess in wrong_guesses:
                print("You've already guessed '" + guess + "' try another letter.")
            else:
                guess_count += 1
                print("That letter is not in the word.")
                print("You have " + (str(8 - guess_count)) + " guesses remaining.")
                wrong_guesses.append(guess)
        if guess_count == 8:
            play_again = input("You lose. Your word was '" + mystery_word + "' Would you like to play again? ")
            if play_again == "no":
                quit()
            if play_again == "yes":
                level = input("Easy, normal, or hard? ")
            if level == "easy":
                mystery_word = random.choice(easy_words).lower()
            elif level == "normal":
                mystery_word = random.choice(normal_words).lower()
            elif level == "hard":
                mystery_word = random.choice(hard_words).lower()
            gameboard = ["_"] * len(mystery_word)
            guess_count = 0
            wrong_guesses = []
            


mysteryword()
