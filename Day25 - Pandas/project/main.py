from turtle import Turtle, Screen
from states import States
import pandas as pd

screen = Screen()
screen.bgpic('Day25 - Pandas/project/blank_states_img.gif')
state_data = pd.read_csv('Day25 - Pandas/project/50_states.csv')
states = States()

while(states.check_state()):
    inputs = screen.textinput("Guess the state name", "Enter the state name: ")
    
    if(inputs == 'exit' or inputs == 'Exit'):
        break

    if(states.guessed_state(inputs) == False):
        states.add_states( inputs, int(state_data[state_data['state'] == inputs].x), int(state_data[state_data['state'] == inputs].y) )

states.save_file(state_data)
