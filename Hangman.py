import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letter:
        used_letter.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letter:
        print("You have already used that letter.")
    else:
        print("Invalid character. Letters only. Try again.")

print(hangman)