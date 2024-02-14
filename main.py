import random
from words_module import word_list
from words_module import hangman_pics

game_start = True
game_running = True
random_word = random.choice(word_list)
blank_list = []
guessed_letters = []
lives = 6


def reset_game():
    global game_start
    global game_running
    global random_word
    global blank_list
    global guessed_letters
    global lives

    game_start = True
    game_running = True
    random_word = random.choice(word_list)
    blank_list = ["_" for _ in random_word]
    guessed_letters = []
    lives = 6


for letter in random_word:
    blank_list.append("_")

while game_running:

    if game_start:
        print(hangman_pics[6])
        print(r"                                               ")
        print(r"  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  ")
        print(r" / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
        print(r"/ __  / (_| | | | | (_| | | | | | | (_| | | | |")
        print(r"\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
        print(r"                   |___/                       ")
        print(r"                                               ")
        game_start = False

    user_input = input("Guess a letter!").lower()

    if user_input in guessed_letters:
        print(f"You've already guessed '{user_input}'. Try again.")
        continue
    guessed_letters.append(user_input)

    # looks over random_word to see if user_input's value is at each index, then changes blank_list's value at that
    # index to user_input value.
    for index, letter in enumerate(random_word):
        if user_input == letter:
            blank_list[index] = letter

    # prints hangman, removes 1 life if wrong letter chosen, and ends game if life = 0
    if user_input in blank_list:
        print(hangman_pics[lives])
    else:
        lives -= 1
        print(hangman_pics[lives])
        print(f"lives left: {lives}")
        if lives <= 0:
            game_running = False
            print(f"You lose!")
            print(f" the word was: {random_word}")
            restart = input("Restart? Type 'Yes' or 'No'").lower()
            if restart == "yes":
                reset_game()

    # checks win condition
    if "_" not in blank_list:
        game_running = False
        print("You won!")
        print(f"The word was: {''.join(blank_list)}")
        restart = input("Restart? Type 'Yes' or 'No'").lower()
        if restart == "yes":
            reset_game()

    print(blank_list)
