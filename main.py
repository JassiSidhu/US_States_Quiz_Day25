import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# add states image on the screen
turtle.shape(image)

TOTAL_STATES = 50
# list to store the correct guesses from user
guess_list = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
states_missed = []

while len(guess_list) < TOTAL_STATES:
    answer_state = screen.textinput(title=f"{len(guess_list)}/50 states correct", prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        if len(guess_list) < TOTAL_STATES:
            for state in all_states:
                if state not in guess_list:
                    states_missed.append(state)
            states_data = pandas.DataFrame(states_missed)
            states_data.to_csv("states_to_learn.csv")
        break

    if (answer_state not in guess_list) and answer_state in all_states:
        state = data[data.state == answer_state]
        guess_list.append(answer_state)
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.goto(float(state.x), float(state.y))
        my_turtle.write(answer_state, align="center", font=('Helvetica', 8, 'normal'))


