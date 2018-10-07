# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:12:07 2018

@author: 28773
"""
import string
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    b=len(secretWord)
    for a in secretWord:
        if a in lettersGuessed:
            b-=1
            break
    if b==0:
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
    # FILL IN YOUR CODE HERE...
    a=''
    for i in secretWord:
        if i in lettersGuessed:
            a=a+i
        else:
            a=a+'_ '
    return a
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a=string.ascii_lowercase
    b=[]
    for i in a:
        b.append(i)
    for i in lettersGuessed:
        if i in b:
            b.remove(i)
    c=''
    for i in b:
        c=c+i
    return c
