print("welcome to treasure island")
print("Your mission is to find treasure")
print("you are on a cross road, where do you wanna go?")
path=input("       Type 'left' or 'right'\n").lower()
if path=='left':
    print("You've come to a lake. There is an island in the middle of the lake")
    wait_swim=input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if wait_swim=='wait':
        wall=input("there are 3 walls- one 'red' one 'yellow' and one 'blue'."
                   "Which one would you like to choose?\n").lower()
        if wall=='yellow':
            print("you win")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")