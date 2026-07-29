import turtle
import pandas

screen = turtle.Screen()
screen.title("USA states game")
image = './day25/USA game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("./day25/USA game/50_states.csv")
states_list = states_data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",prompt="What's another states name? ").title()

    if answer_state== "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./day25/USA game/states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = states_data[states_data.state == answer_state]
        t.goto(states_data.x.item(), states_data.y.item())
        t.write(answer_state)

