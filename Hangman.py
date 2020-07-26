from random import choice
import string

print("H A N G M A N")

words_list = ['python', 'java', 'kotlin', 'javascript']

preview_letters = 0
user_max_tries = 8
used_letters = set()

computer_selection = choice(words_list)
show_letters = computer_selection[0:preview_letters]
hidden_word = show_letters + '-' * (len(computer_selection) - preview_letters)

user_menu = input('Type "play" to play the game, "exit" to quit:')

if user_menu == 'play':

    while user_max_tries > 0:
        print()
        hidden_word_list = list(hidden_word)
        print(hidden_word)
        ask_for_letter = input("Input a letter: ")
        if len(ask_for_letter) == 1:
            if ask_for_letter in string.ascii_lowercase:
                if ask_for_letter in computer_selection and ask_for_letter not in used_letters:
                    for i in range(len(computer_selection)):
                        if computer_selection[i] == ask_for_letter:
                            hidden_word_list[i] = ask_for_letter
                elif ask_for_letter in used_letters:
                    print("You already typed this letter")
                    continue
                elif (ask_for_letter in computer_selection) and (ask_for_letter in used_letters):
                    print("No improvements")
                    user_max_tries -= 1
                else:
                    print("No such letter in the word")
                    user_max_tries -= 1
            else:
                print("It is not an ASCII lowercase letter")
                continue
        else:
            print("You should input a single letter")
            continue
        hidden_word = "".join(hidden_word_list)
        used_letters.add(ask_for_letter)
        if hidden_word == computer_selection:
            print("\n" + hidden_word)
            print("You guessed the word!\nYou survived!")
            break
    else:
        print("You are hanged!")
else:
    quit()