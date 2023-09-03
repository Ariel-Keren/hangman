import functions

def main():
    random_word = functions.get_random_word()
    guessed_letters = []
    number_of_mistakes = 0
    is_game_over = False

    while not is_game_over:
        print(f"\nTotal mistakes: {number_of_mistakes}")
        print(f"Letters already guessed: {', '.join(guessed_letters)}")
        functions.print_word(random_word, guessed_letters)

        guess = functions.get_input(guessed_letters)
        guessed_letters.append(guess)

        if functions.is_mistake(random_word, guess):
            number_of_mistakes += 1
        
        if functions.is_game_won(random_word, guessed_letters):
            functions.print_word(random_word, guessed_letters)
            print("\nYou won! (:")
            is_game_over = True

        elif functions.is_game_lost(number_of_mistakes):
            print("\nYou lost. ):")
            print(f"The word was \"{random_word}\".")
            is_game_over = True

if __name__ == "__main__":
    main()
