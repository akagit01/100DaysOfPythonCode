import random
import data_dict


def store_celeb(celeb1,celeb2):
    #a, b = random.sample(data_dict.celebrities, 2)
    #a,b=random.sample(data_dict.celebrities, 2)
    name1=celeb1['name']
    description1=celeb1['description']
    country1=celeb1['country']
    followers1=celeb1['follower_count']

    name2=celeb2['name']
    description2=celeb2['description']
    country2=celeb2['country']
    followers2=celeb2['follower_count']
    print('*****************************************************************')
    print((f"{name1} who is a {description1} from {country1} with {followers1} \nVS\n {name2} who is a {description2} from {country2} with {followers2}"))
    #return name1,description1,country1,followers1,name2,description2,country2,followers2
    print('*****************************************************************')
    return followers1,followers2

def get_follower_count(celeb1,celeb2):
    #cel1,cel2=get_celebs()
    follower_count1=celeb1['follower_count']
    follower_count2=celeb2['follower_count']
    return follower_count1,follower_count2




#print(f"{name1} who is a {description1} from {country1} \nVS\n {name2} who is a {description2} from {country2}")

def play_lower_higher():
    score=0

    keep_loading=True
    while keep_loading:
        print(f"*** Your current score is : {score} ***")
        celeb1, celeb2 = random.sample(data_dict.celebrities, 2)
        store_celeb(celeb1,celeb2)
        followers1,followers2=get_follower_count(celeb1,celeb2)

        #print(f"follower count for 1 is {followers1} and for 2 is {followers2}")
        #print('*****************************************************************')
        usr_guess = int(input("who has more followers 1 or 2: "))

        if usr_guess==1 and followers1 > followers2:
            print("\n")
            print("Correct")
            print("\n")
            score+=1
        elif usr_guess==2 and followers1 > followers2:
            print("Nope, you are wrong")
            keep_loading=False
        elif usr_guess==2 and followers2 > followers1:
            print("Correct")
            score+=1
        elif usr_guess==1 and followers2 > followers1:
            print("Nope, you are wrong")
            keep_loading=False
        elif followers1==followers2:
            print("both have same no of followers")
            score+=1


    print(f"your final score: {score}")
    return score


play_again = True
final_score=0
while play_again:
    pa = input("Would you like to play higher/lower game? Type y/n: ").lower()
    if pa == 'y':
        final_score = play_lower_higher()
    else:
        print(f"Thanks for playing! Your last score was: {final_score}")
        play_again = False






