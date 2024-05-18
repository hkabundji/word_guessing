import os
import random

secret_word = "iphone" 

tries = 0
tries_limit = 3
print("Welcome to my word guessing game!\n")

letter_guess = input("Guess a letter:\n")
if tries < tries_limit:
    letter_guess = input("Guess a letter:\n")
    print(f"You guessed the letter '{letter_guess}'")


if letter_guess != secret_word: 
    print(False)
else: 
    ("correct")

