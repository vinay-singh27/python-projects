import random
import string
from words import words

def get_valid_word(words) :
    word = random.choice(words)
    if '-' in word or ' ' in word :
        word = random.choice(words)
    return word.upper()

def hangman():

    word = get_valid_word(words)
    word_letters = set(word) #letter of the selected word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    #get user input
    while (len(word_letters) > 0) and (lives > 0) :

        #users word list
        print(f"You have {lives} lives left and you have already used {' '.join(used_letters)}")

        #print the current words
        word_list = [letter if letter  in used_letters else '-' for letter in word]
        print(''.join(word_list))

        user_letter = input('Guess a letter :').upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters :
                word_letters.remove(user_letter)

            else :
                lives -= 1

        elif user_letter in used_letters :
            print('You have already used that letter')

        else :
            print('Invalid Character')

    if lives == 0 :
        print(f"Sorry, you couldn't guess the word. The word was {word}")
    else :
        print(f'Great! You have guess the word {word} and is left with {lives} lives')

    

if __name__ == '__main__' :
    hangman()





