import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman(words):
    
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    lives = 6
    
    while len(word_letters) > 0 and lives!=0:
        print('Lives left are',lives,' and used letters are', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        
        user_letter = input('\nEnter your choice: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
        elif user_letter in used_letters:
            print('You have already tried this character.')
        else:
            print('Invalid Character.')
            
    if lives==0:
        print('You died and word was',word)
    else:
        print('Congrats you win!!! and word was',word)
hangman(words)
