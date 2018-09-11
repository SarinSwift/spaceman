# Spaceman
# Spaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time.

import random


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word




def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for i in secret_word:
        if i not in letters_guessed:
            return False
    #  It won't run this line unless all characters have been guessed
    return True



def get_guessed_words(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    string = ""
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += " _"
    return string


def get_available_letters(letters_guessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new = ""
    for letter in alphabet:
        if letter not in letters_guessed:
            new += letter
    return new

# print(get_available_letters("ac"))

def validate_input(users_input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if users_input in list(alphabet):
        return True
    else:
        return False


def spaceman(secret_word):
    guesses = 12
    length_of_secret_word = str(len(secret_word))
    print("\nThe secret word contains {} letters.".format(length_of_secret_word))

    all_letters_guessed = ""

    while guesses > 0 and is_word_guessed(secret_word, all_letters_guessed) == False:
        letters_guessed = input("\nTake a guess of the letters in the secret word: ")
        letters_guessed = letters_guessed.lower()
        if validate_input(letters_guessed):
            all_letters_guessed += letters_guessed

            if letters_guessed not in secret_word:
                print("Your guess was incorrect: {}".format(get_guessed_words(secret_word, all_letters_guessed)))
            else:
                print("Your guess was correct!: {}".format(get_guessed_words(secret_word, all_letters_guessed)))

            print("Letters chosen: {}".format(get_available_letters(all_letters_guessed)))
            guesses -= 1
            print("Guesses left: {}".format(guesses))

        else:
            print("Please enter 1 lowercase letter!")

    if is_word_guessed(secret_word, all_letters_guessed):
        print("CONGRATULATIONS! You won!")
    else:
        print("\nGAME OVER. You lost!")
        print("The secret word was: {}".format(secret_word))


secret_word = load_word()


if __name__ == "__main__":
    spaceman(load_word())
