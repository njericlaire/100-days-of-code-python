import turtle
import pandas

data=pandas.read_csv("50_states.csv")
all_state=data["state"].to_list()
screen=turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

guess_state=[]
while len(guess_state)<50:

    answer=(screen.textinput(title=f"{len(guess_state)}/50 correct states", prompt="What's another State game?" )).title()
    if answer=="Exit":
        missing_state =[state for state in all_state if state not in guess_state]

        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_to_learn.csv")
        break

    if answer in all_state:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)
        guess_state.append(answer)



turtle.mainloop()

