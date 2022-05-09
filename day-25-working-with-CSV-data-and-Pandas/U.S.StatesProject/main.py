import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Turtle shape is the background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def show_state(coord_x, coord_y, state):
    name_of_state = turtle.Turtle()
    name_of_state.hideturtle()
    name_of_state.penup()
    name_of_state.goto(coord_x, coord_y)
    name_of_state.write(state)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guesses = []
while len(correct_guesses) < 50:
    # Return the guessed state's value properly formatted
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state "
                                                                                              "name?").title()

    # check if the answer_state == "exit" to exit
    if answer_state == "Exit":
        # Generate a csv file that contains the states that have not been guessed
        # if a state out of all states is missing in the guessed_states list it is added to the missing states list
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)  # creates a 1 column dataframe
        new_data.to_csv("states_to_learn.csv")
        break

    # check if the input is equal to a value from column "state"
    if answer_state in data.state.values:
        # don't update the score if it's already guessed
        if answer_state not in correct_guesses:
            guessed_state_x = int(data[data.state == answer_state].x)
            guessed_state_y = int(data[data.state == answer_state].y)
            show_state(guessed_state_x, guessed_state_y, answer_state)
            correct_guesses.append(answer_state)
