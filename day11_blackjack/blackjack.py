import random
from random import *

cards = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 'A']


# ask user if user wants to play
# user should throw 2 cards
# computer will show 1 card
# user is asked if you'd like to hit or pass
# if pass, final card combination is shown
# computer's next card is shown
# if user's card comb is less than com and 21, user won
# com won



def hit(hand):
    new_card = choice(cards)
    if new_card == 'A' and sum(hand) < 11:
        hand.append(1)
    else:
        hand.append(new_card)
    return hand


def pass1(com_card):
    new_card = choice(cards)
    if new_card == 'A' and sum(com_card) < 11:
        new_card = 1
        com_card.append(new_card)
    else:
        com_card.append(new_card)
    return com_card

def check_sum(hand,com_card):
    return sum(hand), sum(com_card)

def check_res(hand, com_card):
    if sum(hand) > sum(com_card) and sum(hand) <= 21:
        print(f'user won with cards {hand} and computer lost with cards {com_card}')
    elif sum(hand) < sum(com_card) and sum(com_card) <= 21:
        print(f'user lost with cards {hand} and computer won with cards {com_card}')
    elif sum(hand) == sum(com_card) and sum(com_card) <= 21:
        print(f"Game drawn with User's cards {hand} and Computer cards {com_card}")
    elif sum(hand)>21 and sum(com_card)<=21:
        print(f'user lost with cards {hand} and computer won with cards {com_card}')
    elif sum(hand)<=21 and sum(com_card)>21:
        print(f'user won with cards {hand} and computer lost with cards {com_card}')



def blackjack():
    hand = sample(cards, 2)
    print(hand)
    com_card = sample(cards, 1)
    print(f"computer's first card: {com_card}")

    sum_user,sum_com=check_sum(hand,com_card)
    user_done=False
    while not user_done and sum_user<21 and sum_com<21 :
        another_card_or_pass = input("Type 'y' to get another card or 'n' to pass: ").lower()
        if another_card_or_pass == 'y':
            hit(hand)
            print(f"users card after hit: {hand}")
            pass1(com_card)
            print(f"dealer's cards: {com_card}")
            sum_user,sum_com=check_sum(hand,com_card)
            print(f"user's card sum is {sum_user} and computers cards sum is {sum_com}")
            if sum_user>21 or sum_com>21:
                break


        elif another_card_or_pass== 'n':
            pass1(com_card)
            sum_user, sum_com = check_sum(hand, com_card)
            user_done=True
            #check_res(hand, com_card)

    check_res(hand,com_card)

continue_playing = True

while continue_playing:
    play = input("do you want to play black jack? y/n: ").lower()
    if play == 'y':
        blackjack()
    else:
        continue_playing = False

