from random import choice
from urllib.request import urlopen

def get_input(guessed_letters: list[str]):
    while True:
        user_input = input("\n\nType your guess:\n").lower().replace(" ", "")
        if len(user_input) == 1 and "a" <= user_input <= "z" and user_input not in guessed_letters:
            return user_input
        print("Invalid input. Try again.")

def get_random_word():
    WORDS_URL = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urlopen(WORDS_URL)
    txt = response.read()
    words = txt.splitlines()
    return str(choice(words))[2:-1]

def print_word(random_word: str, guessed_letters: list[str]):
    print()
    for letter in random_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

def is_game_won(random_word: str, guessed_letters: list[str]):
    for letter in random_word:
        if letter not in guessed_letters:
            return False
    return True

def is_game_lost(number_of_mistakes: int):
    MAXIMUM_NUMBER_OF_MISTAKES = 7
    return number_of_mistakes == MAXIMUM_NUMBER_OF_MISTAKES

def is_mistake(random_word: str, guess: str):
    return guess not in random_word
