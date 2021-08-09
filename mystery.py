# choose difficulty: easy(4-6), normal(6-8), hard(8+)
# sort words by length, select words from list within range of level
# ensure random word does not change

# ???import the random module
# ???import random
import random

# declares needed global variable
mystery_word = ""


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
    guess_count = 0
    wrong_guesses = []

    # sets mystery word/level based on input
    def start_game():
        global mystery_word
        level = input("Easy, normal, or hard? ")
        if level == "easy":
            mystery_word = random.choice(easy_words).lower()
        elif level == "normal":
            mystery_word = random.choice(normal_words).lower()
        elif level == "hard":
            mystery_word = random.choice(hard_words).lower()
        # reassigns global variable

    guess_another = "yes"
    start_game()
    gameboard = ["_"] * len(mystery_word)
    print("Your word has " + str(len(mystery_word)) + " letters.")
    print(mystery_word)
    while guess_another == "yes":
        print(" ".join(gameboard))
        guess = input("Please guess a letter ")

        if guess in mystery_word:
            start = 0
            while mystery_word.find(guess, start) != -1:
                index = mystery_word.index(guess, start)
                gameboard[index] = guess
                start = index + 1
        else:
            if guess in wrong_guesses:
                print("You've already guessed '" + guess
                      + "' try another letter.")
            else:
                guess_count += 1
                print("That letter is not in the word.")
                print("You have " + (str(8 - guess_count))
                      + " guesses remaining.")
                wrong_guesses.append(guess)
        if mystery_word == ("".join(gameboard)):
            print("")
            print("                     /|")
            print("       =  =  =      / |")
            print("  ____| || || |____/  | -_-_-_-_-_-_")
            print("|)----| || || |____   | YOU WIN!!!")
            print("  ((  | || || |  ))\  | _-_-_-_-_-_-")
            print("   \\\_|_||_||_|_//  \ |")
            print("    \___________/    \|")
            print("")
            play_again = input("Would you like to play again? ")
            if play_again == "no":
                guess_another = "stop"
            if play_again == "yes":
                start_game()
                guess_count = 0
                gameboard = ["_"] * len(mystery_word)
                print("Your word has " + str(len(mystery_word)) + " letters.")
        if guess_count == 8:
            print("")
            print("     .-''''''-.  ")
            print("   .'          '. ")
            print("  |   O      O   |")
            print(" :           `    :")
            print(" |                |   ")
            print(" :    .------.    :")
            print("  |  '        '  |")
            print("   '.          .'")
            print("     '-......-'")
            print("")
            play_again = input("You lose. Your word was '" + mystery_word
                               + "' Would you like to play again? ")
            if play_again == "no":
                guess_another = "stop"
            if play_again == "yes":
                start_game()
                guess_count = 0
                gameboard = ["_"] * len(mystery_word)
                print("Your word has " + str(len(mystery_word)) + " letters.")


mysteryword()
