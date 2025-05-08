import random

def deal_card():
    """ returns a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if c_score==u_score:
        return "Draw"
    elif c_score==0:
        return "Lose, opponent has blackjack"
    elif u_score==0:
        return "Won, You have a blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Com went over, You win."
    elif u_score > c_score:
        return "You win"
    else:
        return "You Lose"

user_cards=[]
com_cards=[]
com_score=-1 #cannot set it to 0 as that will be blackjack
user_score=-1
is_game_over=False

for _ in range(2):
    user_cards.append(deal_card())
    com_cards.append(deal_card())


while not is_game_over:
    user_score=calculate_score(user_cards)
    com_score=calculate_score(com_cards)
    print(f"your cards: {user_cards}, your score: {user_score}")
    print(f"dealer's first card: {com_cards[0]}")

    if user_score==0 or com_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_Deal=input("y for another card or n to pass: ").lower()
        if user_should_Deal=='y':
            user_cards.append(deal_card())
        else:
            is_game_over=True

while com_score !=0 and com_score < 17:
    com_cards.append(deal_card())
    com_score = calculate_score(com_cards)



compare(user_score,com_score)
