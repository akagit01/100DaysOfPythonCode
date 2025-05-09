import random
import data_dict



def format_data(account):
    name1 = account['name']
    description1 = account['description']
    country1 = account['country']
    #followers1 = account['follower_count']
    return (f"{name1}, a {description1}, from {country1}  ")

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess=='a'
    else:
        return user_guess=='b'

score=0
game_continue=True
account_b=random.choice(data_dict.celebrities)

while game_continue:
    account_a = account_b
    account_b = random.choice(data_dict.celebrities)
    if account_a==account_b:
        account_b=random.choice(data_dict.celebrities)

    print(f"compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    followers1=account_a['follower_count']
    followers2=account_b['follower_count']

    usr_guess = input("who has more followers 'A' or 'B': ").lower()

    #clear screen
    print("\n" * 20)

    is_correct= check_answer(usr_guess, followers1,followers2)

    #give user feedback on guess
    if is_correct:
        score+=1
        print(f"You are right.current score {score}")
    else:
        print(f"sorry you are wrong. Final score {score}")
        game_continue=False






