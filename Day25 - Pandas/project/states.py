from turtle import Turtle
import pandas

class States():
    def __init__(self):
        self.state = []

    def add_states(self, name, x, y):
        temp_state = Turtle()
        temp_state.penup()
        temp_state.hideturtle()
        temp_state.color('black')
        temp_state.goto(x, y)
        temp_state.write(name)
        temp_state.state_name = name
        self.state.append(temp_state)
    
    def check_state(self):
        if(len(self.state) < 50):
            return True
        return False

    def guessed_state(self, name):
        for turtle_obj in self.state:
            if turtle_obj.state_name == name:
                return True
        return False

    def save_file(self, data):
        print("entered")
        unguessed_name = []

        guessed_names = [obj.state_name for obj in self.state]

        for name in data['state']:
            if name not in guessed_names:
                unguessed_name.append(name)

        df = pandas.DataFrame(unguessed_name, columns=['Unguessed State Name'])
        df.to_csv('Day25 - Pandas/project/unguessed_states.csv', index=False) 