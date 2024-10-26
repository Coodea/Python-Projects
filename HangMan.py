import random
from words import wordss
import string

def get_valid_word(wordss):
    word = random.choice(wordss)
    while '-' in word or ' ' in word:
        word = random.choice(wordss) 

    return word.upper()

def hangman():
    word = get_valid_word(wordss)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, 'lives left.')
        print('You have used these letters: ', ' '.join(used_letters))
        wordlist = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(wordlist))

        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print('The letter is not in the word, you lose a life.')
        elif user_letter in used_letters:
            print('You have already used that character. Try again.')
        else:
            print('Invalid character. Try again.')

    if lives == 0:
        print("You died, the word was", word)
        exit()
    else:
        print('You guessed the word', word, '!!')
    
if __name__ == '__main__':
    hangman()
