# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    n = 0
    
    for letter in secretWord:
        if letter in lettersGuessed:
            n += 1
    
    return n == len(secretWord)
    
def getGuessedWord(secretWord, lettersGuessed): 
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            word = word + letter + ' '
        else:
            word = word + '_' + ' '
    
    return word 
                        

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    remaining = list(string.ascii_lowercase)
    
    for letter in lettersGuessed:
        if letter in remaining:
            remaining.remove(letter)
    
    return ''.join(remaining)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    
    n = 8
    guess = []
    flag = False
    
    while n > 0:
        #Initial Statements
        print('You have {} guesses left.'.format(n))
        left = getAvailableLetters(guess)
        print('Available letters: {}'.format(left))
        
        #Ask user for input
        letter = input('Please enter a letter: ').lower()
        
        #Chech if the input letter is already in the guess 
        if letter in guess:
            string = getGuessedWord(secretWord, guess)
            print("Oops! You've already guessed that letter: {}".format(string))
            continue
        else:
            guess.append(letter)
            
        #Chech if the letter is in the secret word     
        if letter in secretWord:
            string = getGuessedWord(secretWord, guess)
            print('Good guess: {}'.format(string)) 
        else:
            string = getGuessedWord(secretWord, guess)
            print('Oops! That letter is not in my word: {}'.format(string))
            n -= 1
        
        #Check if the word is guessed completely 
        if isWordGuessed(secretWord, guess):
            flag = True
            break
        
    if flag:
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was {}'.format(secretWord)) 
            
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord) 
