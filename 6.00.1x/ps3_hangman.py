# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # convert secretword into list
    sword = list(secretWord)
    flagcounter = 0
    for char in sword:
        if char in lettersGuessed:
            flagcounter += 1
    
    if (flagcounter == len(secretWord)):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    index = 0
    displayword = []
    
    for i in range(len(secretWord)):
        displayword.append("-")
        
    for char in secretWord:
        if char in lettersGuessed:
            displayword[index] = char
        
        
        index += 1
        
    return " ".join(displayword)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    alphabets = string.ascii_lowercase
    alphabets = list(alphabets)
    clone = alphabets[:]
    
    for char in clone:
        if char in lettersGuessed:
            alphabets.remove(char)
        
        
    return "".join(alphabets)


def correctguess(secretWord, guess):
    """
    takes in 2 argument secretword and a single char guess
    returns true if guess is correct else false
    """
    if guess in secretWord:
        return True
    else:
        return False
    

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
    chances = 8
    lettersguessed = []
    winflag = False
    #availableletters = getAvailableLetters(lettersguessed)
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    
    while (chances != 0):
        print("You have", chances, "guesses left")
        print("Available letters:", getAvailableLetters(lettersguessed))
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        
        if guess in lettersguessed:
            print("You have already guessed this letter. Plz try again")
            continue
        
        lettersguessed.append(guess)
               
        if (correctguess(secretWord, guess)):
            if (isWordGuessed(secretWord, lettersguessed)):
                print("Good guess:", getGuessedWord(secretWord, lettersguessed))
                winflag = True
                break
            else:
                print("Good guess:", getGuessedWord(secretWord, lettersguessed))
                continue
        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersguessed))
            chances -= 1
            continue
        
    if (winflag):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord)
        

            






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
