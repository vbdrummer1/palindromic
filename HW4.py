import re
import random
import os
import sys


def clean_sentence(sentence):
    return re.sub(r'[^A-Za-z]', '', sentence.lower())


def get_rand_word(difficulty_words):
    return difficulty_words[random.randrange(0, len(difficulty_words))]


def get_words_min_max_length(words, min_length, max_length):
    difficulty_words = []
    for word in words:
        if len(word) >= min_length and len(word) <= max_length:
            difficulty_words.append(word)
    return difficulty_words


def get_words_for_difficulty(words, choice):
    if choice == 'easy':
        return get_words_min_max_length(words, 4, 6)
    elif choice == 'medium':
        return get_words_min_max_length(words, 6, 8)
    else:
        return get_words_min_max_length(words, 8, 99)


def get_all_words():
    with open('/usr/share/dict/words', 'r') as dictionary:
        words = []
        for word in dictionary.readlines():
            words.append(clean_sentence(word))
        return words


def get_difficulty_level():
    level = input("Enter 1 for easy, 2 for medium, any other key for hard: ")
    if level == "1":
        return "easy"
    elif level == "2":
        return "medium"
    else:
        return "hard"


def draw(bad_guesses, good_guesses, mystery_word):
    clear()
    print('Strikes: {}/8'.format(len(bad_guesses)))
    print('')
    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')
    for letter in mystery_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_ ', end='')
    print('')


def clear():
    os.system('clear')


def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def play(done, difficulty_words):
    mystery_word = get_rand_word(difficulty_words)
    bad_guesses = []
    good_guesses = []
    while True:
        draw(bad_guesses, good_guesses, mystery_word)
        guess = get_guess(bad_guesses, good_guesses)
        if guess in mystery_word:
            good_guesses.append(guess)
            found = True
            for letter in mystery_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print("You win!")
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, mystery_word)
                print("You lost!")
                print('You did not get the word.')
                done = True
        if done:
            play_again = input("Play again? Y/n ").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()


def welcome():
    start = input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print("Bye!")
        sys.exit()
    else:
        return True


def main():
    choice = get_difficulty_level()
    words = get_all_words()
    difficulty_words = get_words_for_difficulty(words, choice)
    done = False
    play(done, difficulty_words)


if __name__ == '__main__':
    main()
