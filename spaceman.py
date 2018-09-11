# Spaceman
# Spaceman is a guessing game. There is a mystery word which the user tries to guess one letter at a time.
import random

def load_words():

    file = open('words.txt', 'r')
    # reads every line in the file and returns a lost containing the line.
    line = file.readline()
    # breaks the lines down to single words by seperating from the spaces.
    words_list = line.split()
    file.close()
    # this will randomly generate a single word from many of the words created
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    rounds = 0
    for i in secret_word:
        if i in letters_guessed:
            rounds += 1
    if rounds == len(secret_word):
        return true
    else:
        return false

def get_guessed_words(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # creates the line were if you guessed the letter correctly, it will replace the _ with that letter.
    # and if it wasnt guessed correctly, it will put in an _
    string = ""
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += "_ "
    return string

def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = ""
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    # if a letter wasnt guessed, it will append all the letters into an empty string
    for i in alphabet:
        if i not in letters_guessed:
            string += i
    return string

def spaceman_graphic(guesses_left):
    if guesses_left == 11:
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
    if guesses_left == 10:
        print("              ")
        print("       O      ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
    if guesses_left == 9:
        print("              ")
        print("       O      ")
        print("       |      ")
        print("              ")
        print("              ")
        print("              ")
    if guesses_left == 8:
        print("              ")
        print("       O      ")
        print("      /|      ")
        print("              ")
        print("              ")
        print("              ")
    if guesses_left == 7:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("              ")
        print("              ")
        print("              ")
    if guesses_left == 6:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      /       ")
        print("              ")
        print("              ")
    if guesses_left == 5:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("              ")
    if guesses_left == 4:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("   /          ")
    if guesses_left == 3:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("   / /        ")
    if guesses_left == 2:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("   / / |      ")
    if guesses_left == 1:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("   / / | \    ")
    if guesses_left == 0:
        print("              ")
        print("       O      ")
        print("      /|\     ")
        print("      / \     ")
        print("              ")
        print("   / / | \ \  ")
        print("Oh no! spaceman left earth")
        print("GAME OVER!")

def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # prints the lenght of the secret word
    len_secret_word = str(len(secret_word))

    print("\nThe secret word contains {} letters.".format(len_secret_word))
    guesses_left = 12
    letters_guessed = []

    # It will continue itersating through this while loop until 0
    while guesses_left >= 0:
        print("************")
        # if the secret_word doesnt == the whole word that users have guessed,
        # ex. secretword = "snow", get_guessed_words = sn_w, it will keep going through this if statement
        if secret_word != get_guessed_words(secret_word, letters_guessed):
            print("You have {} guesses left.".format(str(guesses_left)))
            spaceman_graphic(guesses_left)
            print("Letters available: {}".format(get_available_letters(letters_guessed)))
            user_guess = input("Take a guess! You can only input one single letter: ")
            # turns all the input into a lower case so it matches the alphabet variable I created
            user_guess = user_guess.lower()

            # checks to see if the user have already guessed that letter
            if user_guess in letters_guessed:
                print("You have already guessed that letter! {}".format(get_guessed_words(secret_word, letters_guessed)))
            # if the guessed letter is not in the secret word:
            elif user_guess not in secret_word:
                print("\n\nOops! That letter is not in the secret word {}".format(get_guessed_words(secret_word, letters_guessed)))
                guesses_left -= 1
            # otherwise, you guessed the correct letter
            else:
                letters_guessed.append(user_guess)
                print("\nYou got it! {}".format(get_guessed_words(secret_word, letters_guessed)))
            # this will append the users guessed letter into the letters_guessed variable
            letters_guessed.append(user_guess)
        # if the secret_word == the whole word that the user guessed
        elif secret_word == get_guessed_words(secret_word, letters_guessed):
            print("Congratulations! You won!")
            break
    # else, it ran out of turns, and will print game over
    else:
        print("************")
        print("GAME OVER: {}".format(secret_word))

# uses to run the code below
# if we dont have this, it wont call the functions below????
if __name__ == '__main__':
    print("Spaceman game starting!")
    spaceman(load_words())
