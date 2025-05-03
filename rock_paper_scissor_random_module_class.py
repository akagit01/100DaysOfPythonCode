from random import choice

# Define ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store choices and arts
dict1 = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}
art = {0: rock, 1: paper, 2: scissors}

usr_score = 0
com_score = 0
count = 3

while count != 0:
    usr_choice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
    usr_choice2 = dict1.get(usr_choice)
    print(f"Your choice: {usr_choice2}")
    print(art[usr_choice])

    com_choice = choice([0, 1, 2])
    com_choice2 = dict1.get(com_choice)
    print(f"Computer's choice: {com_choice2}")
    print(art[com_choice])

    if usr_choice == com_choice:
        print("It's a Draw!")
        usr_score += 1
        com_score += 1
        count += 1
    elif (usr_choice == 0 and com_choice == 2) or (usr_choice == 1 and com_choice == 0) or (usr_choice == 2 and com_choice == 1):
        print("You win this round!")
        usr_score += 1
    else:
        print("Computer wins this round!")
        com_score += 1

    count -= 1
    print(f"Chances left: {count}")

# Final result
print("\nGame Over!")
if com_score > usr_score:
    print(f"Computer won. Computer Score: {com_score} | Your Score: {usr_score}")
elif usr_score > com_score:
    print(f"You won! Computer Score: {com_score} | Your Score: {usr_score}")
else:
    print(f"It's a tie! Computer Score: {com_score} | Your Score: {usr_score}")
