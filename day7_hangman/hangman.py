from random import *
from list_of_words import words
#create  a list with words



#select a random word from list

word=choice(words).lower()
#print(word)
#create a list with '_' of the length same as that of random word

blank_list=[]
for letter in word:
    blank_list.append('_')

print(blank_list)


#give user 5 chances
life=len(word)

game_over=False


#on correct guess, replace '_' with the correct guess letter, move to next turn until life remains
while not game_over:
    # ask user to guess one letter a time
    print(f"you have {life} chances to guess the right word")
    user_guess = input('Please guess a letter: ').lower()
    print(f"you guessed:  {user_guess}")

    #check if guessed letter exists in word
    if user_guess in word:  #returns true if it does
        life = life - 1

        for idx, letter in enumerate(word):
            if letter==user_guess:  #checks if guessed letter matches any letter in word
            #idx=word.index(user_guess)
                blank_list[idx]=user_guess  #replaces '_' with guess
        print(blank_list)

    else:
        # on wrong guess, subtract a life, move to next tuen until life remains
        life=life-1


    if life==0:
        game_over=True

blank_list=''.join(blank_list)
#if all attempts completed, and all were correct, user won game over
if blank_list==word:
    print(f"congrats, you guessed the word- {blank_list}")
#if all attempts completed, not all were correct, user lost
else:
    print(f"sorry game over. You lost. Your guessed word= {blank_list}")
    


