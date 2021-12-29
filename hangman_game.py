#Welcome to the hangman game
#In this game computer choose a word from a wordlist
#Then user tries to guess the letters of the word
#If user guess a letter which is not present in the word than one element is added to the diagram
#If the hangman stick diagram gets completed before player guess all the letters then player lost his game
import random
from hangman import hangman_stages

s = len(hangman_stages.stages)

q='''
 _        ___ ______  __  _____             ____  _       ____  __ __ 
| |      /  _]      ||  |/ ___/            |    \| |     /    ||  |  |
| |     /  [_|      ||_ (   \_             |  o  ) |    |  o  ||  |  |
| |___ |    _]_|  |_|  \|\__  |            |   _/| |___ |     ||  ~  |
|     ||   [_  |  |      /  \ |            |  |  |     ||  _  ||___, |
|     ||     | |  |      \    |            |  |  |     ||  |  ||     |
|_____||_____| |__|       \___|            |__|  |_____||__|__||____/ '''
print(q)
print("!Welcome to the Hangman game")
word_list=["cute",'beautiful','handsome','ugly']
#randomly choose a word from word_list
chosen_word = random.choice(word_list)


display = []
for i in range(len(chosen_word)):
    display.append("_")

a = ''
a=a.join(display)
print(a)
lives = 6
end = False
while True:
    if lives == 0:
        break
    else:
        while not end:
            guess = input("Guess a letter:").lower()
            if guess in chosen_word:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        display[i] = guess
                        if guess in display:
                            print("already guessed try something else")


                print(f"{''.join(display)}")
                if "_" not in display:
                    end = True
                    print("win")
                    break
            else:
                print(guess,"not there")
                if lives == 0:
                    print(hangman_stages.stages[lives])
                    print("you lose")
                    break
                print(hangman_stages.stages[lives])
                lives -= 1

print("Game over")