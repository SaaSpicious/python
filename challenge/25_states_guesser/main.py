import turtle
import pandas

def process_guess(answer, states_data, guessed_states):
    if states_data[states_data.state == answer].empty:
        print("No correct state!")
    else:
        guessed_states.append(answer)
        print(guessed_states)
        display_state(states_data[states_data.state == answer])
    return guessed_states

def display_state(state_dataset):
    state = turtle.Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.goto(int(state_dataset.x.item()),int(state_dataset.y.item()))
    turtle.write(f"{str(state_dataset.state.item())}", move=False, align="center",font=("Arial", 8, 'bold'))


def save_missed_states(guessed_states,states_data):
    missed_states = [n for n in states_data if n not in guessed_states]
    return missed_states


data_path = './50_states.csv'
states_data = pandas.read_csv(data_path)

screen = turtle.Screen()
screen.title("Guess US States")

image = "blank_states_img.gif"

screen.addshape(image)
map = turtle.Turtle()
map.shape(image)

answer_state = ""
guessed_states = []

while answer_state.lower() != "exit":
    answer_state = screen.textinput(title="Guess a state!", prompt="What's another name of a US State that you know?").title()
    guessed_states = process_guess(answer_state,states_data, guessed_states)


print(save_missed_states(guessed_states,states_data))
print(f"Congratulations, you guessed {len(guessed_states)} states correctly!")
