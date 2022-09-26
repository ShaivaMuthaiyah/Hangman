
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages
import random


print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guessed = []


#print(f'test, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    

    if guess in guessed:
        print(f"You have guessed -{guess}- already\n")
    

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
      
        print(f"You guessed -{guess}- which is not in the word\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")
    guessed.append(guess)

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])