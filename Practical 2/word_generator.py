"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.

@author: edmundpjc
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter your word format: ")).lower()
word = ""
for kind in word_format:
    if kind == CONSONANTS.strip():
        word += random.choice(CONSONANTS)
    elif kind == VOWELS.strip():
        word += random.choice(VOWELS)

print(word)