from random import *

Easy_level_attempts=10
Hard_level_attempts=5
num=randint(1,100)
print(num)

def set_level():
    level = input("choose e for easy or h for hard: ")
    if level == 'h':
        return Hard_level_attempts
    else:
        return Easy_level_attempts


def guess_the_no():
    user_attempts=set_level()
    print(f"you have total {user_attempts} chances")
    while user_attempts!=0:
        user_attempts = user_attempts - 1

        guess=int(input("make a guess"))
        if num==guess:
            print("That's right. You won")
            break
        elif num-guess > 50:
            print("your guess is too low")
        elif num-guess < 50 and num-guess > 20:
            print("your guess is low")
        elif num-guess <20 and num-guess > 10:
            print("close")
        elif num-guess <=10:
            print("very close")
        print(f"you have {user_attempts} left")
play_again=True
while play_again:
    again=input("do you wish to play Guess The Number Game? y/n: ").lower()
    if again=='y':
        guess_the_no()
    elif again=='n':
        play_again=False
    else:
        print('please enter y/n')


