import random


def main():
    while True:
        player_action = str(
            input('Type "play" to play the game, type "exit" to quit: '))
        if player_action == 'exit':
            quit()
        elif player_action == 'play':
            print('H A N G M A N')
            word_list = ['python', 'java', 'kotlin', 'javascript']
            secret_word = list(random.choice(word_list))
            current_state = list('-' * len(secret_word))
            incorrect_guesses = 0
            letters_guessed = []
            while incorrect_guesses < 8:
                print()
                print(''.join(current_state))
                if current_state == secret_word:
                    print('You guessed the word!\nYou survived!')
                    quit()
                guess = str(input('Input a letter: '))
                if len(guess) != 1:
                    print('You should input a single letter')
                elif not guess.isascii() or not guess.isalpha() or not guess.islower():
                    print('Please enter a lowercase English letter')
                elif guess in set(letters_guessed):
                    print("You've already guessed this letter")
                elif guess in secret_word:
                    indicies = [i for i, letter in enumerate(
                        secret_word) if letter == guess]
                    for index in indicies:
                        current_state[index] = guess
                else:
                    print("That letter doesn't appear in the word")
                    incorrect_guesses += 1
                letters_guessed.append(guess)
            print('You lost!')


if __name__ == '__main__':
    main()
