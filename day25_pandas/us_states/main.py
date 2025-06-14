import turtle
import pandas

screen=turtle.Screen()
screen.title("US states game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score=0
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states corrent"
                                    , prompt="What's another state's name?").title()

    if answer_state == "Exit":
        remaining_states = []
        for state in all_states:
            if state not in guessed_states:
                remaining_states.append(state)

        rem_states_df = pandas.DataFrame(remaining_states)
        rem_states_df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data=data[data.state == answer_state]
        xcor=int(state_data["x"].item())
        ycor=int(state_data["y"].item())
        score+=1
        turtle.pu()
        turtle.goto(xcor,ycor)
        turtle.write(answer_state)




screen.exitonclick()



