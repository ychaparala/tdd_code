# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 15:58:17 2014

@author: Evan
"""

# Obtain data from text-file
with open('../data/three_letter_word_list.txt') as word_list_file:
    wordlist = [x.rstrip() for x in word_list_file.readlines()]

# Store Data Like this
guesses = [("cab", 1), ("fed", 2)]

# select random word
import random
from functools import reduce
wordlist[random.randint(0, len(wordlist))]

# define get word function


def pickword():
    word = wordlist[random.randint(0, len(wordlist))].lower()
    return word

# Get name and Welcome the User


def getname():
    print("Welcome to the three letter word game!")
    name = input("What is your name? ")
    print("Welcome, " + name)
    return name

# Define show guesses


def print_info(guesses, guesses_allowed):
    if len(guesses) < 1:
        print("You haven't made any guesses yet.")
    else:
        print("You have guessed the following:\n")
        for i in guesses:
            print(i[0] + " had " + str(i[1]) + r" letter(s) in common.")
        print("You have " + str(guesses_allowed) + " guesses remaining.")

# Prompt User for Guess, check it is correct length


def ask_for_guess(name):
    while True:
        word_guess = input(
            "Hello " +
            name.capitalize() +
            ". \n Please enter the three letter word you would like to guess (or type quit): ")
        if word_guess.lower() == "quit":
            return word_guess
        elif len(word_guess) != 3:
            print("Please enter a THREE letter word.")
        elif any([i.isdigit() for i in word_guess]):
            print("Do not enter numbers.")
        else:
            return word_guess

# Compare the words


def compare_words(guess, real_word):
    number_in = 0
    for letter in guess:
        if letter in real_word:
            real_word = real_word.replace(letter, "", 1)
            number_in += 1
    return(guess, number_in)

# Global Variable Declaration
chosen_word = pickword()
guesses = []
guesses_allowed = 5

# Start Game
name = getname()

while True:
    print_info(guesses, guesses_allowed)
    guess = ask_for_guess(name)
    guesses_allowed = guesses_allowed - 1
    if guess == chosen_word:
        print("You won!")
        break
    elif guess.lower() == "quit":
        print("Goodbye")
        break
    elif guesses_allowed < 1:
        print("Sorry, you ran out of guesses. The word was: " + chosen_word)
        break
    else:
        result = compare_words(guess, chosen_word)
        guesses.append(result)


# J-Raj version
def CommonLetters(s1, s2):
    return [x for x in list(s1) if x in list(s2)]
CommonLetters("goo", "god")


range(10)

var1 = range(5)
var2 = range(5)
x = [var1, var2]
reduce(lambda var1, var2: var1 + var2, x)


result = []
for letter in "45the":
    result.append(letter.isdigit())

any([letter.isdigit() for letter in "the45"])

"45the".isdigit()


random.randint(0, 1)
