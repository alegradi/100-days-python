import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read State csv
state_data = pandas.read_csv("50_states.csv")
states = state_data.state


# Check if a certain state is in the data
def check_state(state_to_check):
    check_state = state_data[state_data.state == state_to_check]
    if len(check_state) != 0:
        return True
    else:
        return False


# Use turtle to write to map
def write_to_map(write_state, x_coordinate, y_coordinate):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.color("black")
    text.goto(x_coordinate, y_coordinate)
    text.write(write_state, align="left", font=('Arial', 8, 'normal'))


# Write state name to map
def write_state_to_map(state_to_write):
    data_item = state_data[state_data.state == state_to_write]
    x_coordinate = float(data_item["x"])
    y_coordinate = float(data_item["y"])

    # Debug info below
    # print(data_item)
    # print(type(x_coordinate))
    # print(f"X: {x_coordinate}, Y: {y_coordinate}")

    write_to_map(state_to_write, x_coordinate, y_coordinate)
    correct_guesses.append(state_to_write)


correct_guesses = []
all_states = state_data.state.to_list()

while len(correct_guesses) < 50:

    answer_state = screen.textinput(f"Guess the State! {len(correct_guesses)}/50",
                                    "What's another State?").title()

    # Use 'exit' to exit the game
    if answer_state == "Exit":

        # Save the list of unentered states to it`s own csv
        missing_states = [missing_state for missing_state in all_states if missing_state not in correct_guesses]

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if check_state(answer_state) and answer_state not in correct_guesses:
        write_state_to_map(answer_state)
