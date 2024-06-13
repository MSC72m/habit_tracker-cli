import json
from datetime import datetime, timedelta
import textwrap

def load_habits():
    try:
        with open('habits.json', 'r') as file:
            habits = json.load(file)
    except FileNotFoundError:
        print("Habits file not found. Creating a new one.")
        habits = []
    except json.decoder.JSONDecodeError:
        print("Habits file contains invalid JSON. Resetting to empty.")
        habits = []
    return habits

def save_habits(habits):
    try:
        with open("habits.json", 'w') as file:
            json.dump(habits, file)
    except FileNotFoundError:
        error = print("File does not exist, check to see if it's loaded")
        return error


def add_habit(habits):
    try:
        name = input("What's the name of the habit you want to add? ")
        if name == "":
            raise ValueError("Empty string")
        if not name.isalpha():
            raise ValueError("No numbers or special characters allowed, only letters")

        time = str(datetime.now().date())
        habit = dict(name=name, streak=0, modified_time=time)
        habits.append(habit)
        print(f"{habit['name']} has been added")
    except ValueError as e:
        print(e)



def complete_habit(habits):
    number = get_number(habits)
    if number is None:
        return
    habit = habits[number-1]
    streak = habit['streak']
    habit['streak'] = streak + 1
    print(habit['streak'])
    


def view_habits(habits):
    leng = len(habits)
    for habit in habits:
        print(f"name: {habit['name']}, streaks: {habit['streak']}, last update: {habit['modified_time']}")


def remove_habits(habits):
    number = get_number(habits)
    if number is None:
        return
    number -= 1
    del habits[number]


def get_number(habits):
    i = 0
    print("Habits: ")
    for habit in habits:
        i += 1
        if 'name' in habit:
            print(f"{i}) {habit['name']}", end='')
            print(', ', end='')
    print()
    leng = len(habits)
    try:
        command = input("Enter the index of the habit you want to remove: ")
        if command == "":
            raise ValueError("Empty input")
        if not command.isdigit():
            raise ValueError("Input must be a number")
        number = int(command)
        if not 1 <= number <= leng:
            raise ValueError(f"Number must be between 1 and {leng}")
    except ValueError as e:
        print(e)
        return None
    return number


def main():
    while True:
        habits = load_habits()
        valid_inputs = ['1', '2', '3', '4', '5', 'q']
        command = input(" 1) Enter 1 for adding a habit \n 2) Enter 2 inorder to add to you streak a habit \n 3) Enter 3 to view current Habits \n 4) Enter 4 to remove an habit from the list \n 5) Enter 5 or q for quitting \n")
        if command in valid_inputs:
            if command == valid_inputs[0]:
                add_habit(habits)
            elif command == valid_inputs[1]:
                complete_habit(habits)
            elif command == valid_inputs[2]:
                view_habits(habits)
            elif command == valid_inputs[3]:
                remove_habits(habits)
            elif command == valid_inputs[-1]:
                break
            elif command == valid_inputs[-2]:
                break
            save_habits(habits)


if __name__ == "__main__":
    main()