import os
import random

secret_word = "iphone" 

tries = 0
word_guess = 0
limit = 3
letter_guess_limit = 3
word_guess_limit = 3
letter_guess = []

print("Welcome to my word guessing game!\n")

letter_guess = input("Guess a letter:\n")
if tries < letter_guess_limit and word_guess < word_guess_limit:
    letter_guess = input("Guess a letter:\n")
    print(f"You guessed the letter '{letter_guess}'")


if letter_guess != secret_word: 
    print(False)
else: 
    ("correct")

if word_guess >= word_guess_limit:
    print("yikes you ran out of guesses")

if letter_guess >= letter_guess_limit:
    print("oops no more guesses. Better luck next time!")

if letter_guess == secret_word:
    print("you did it yay!")  