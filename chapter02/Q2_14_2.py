import random
import string

lowercase_letters = list(string.ascii_lowercase)
random.shuffle(lowercase_letters)

for letter in lowercase_letters:
    print(letter)
    if letter == "n":
        break
