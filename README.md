# Habit Tracker

## Project Description
This project is a command-line habit tracker that allows users to add, complete, view, and remove habits. The habit data is stored in a JSON file (`habits.json`), ensuring persistence across sessions.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Functionality](#functions-and-functionality)
- [Code Explanation](#code-explanation)

## Installation
1. Clone the repository.
2. Ensure you have Python installed on your system.
3. Ensure you have a `habits.json` file in the same directory as the script. If not, the script will create an empty one for you.

## Usage
To run the project, use the following command:
```bash
python habit_tracker.py
```
This will start the command-line interface for managing your habits.

## Functions and Functionality
### load_habits()
Loads habits from the habits.json file.
Handles file not found and JSON decode errors.
### save_habits(habits)
Saves the habits to the habits.json file.
Handles errors that may occur during the save process.
### add_habit(habits)
Prompts the user to add a new habit.
Validates the input and appends the new habit to the list.
### complete_habit(habits)
Prompts the user to select a habit to complete.
Increments the streak of the selected habit.
### view_habits(habits)
Displays the list of current habits with their streaks and last update times.
### remove_habits(habits)
Prompts the user to select a habit to remove.
Removes the selected habit from the list.
### get_number(habits)
Prompts the user to select a habit by index.
Validates the input and returns the selected habit index.
### main()
Main loop to handle user commands for adding, completing, viewing, and removing habits, or quitting the application.

## Code Explanation
Importing Libraries
``` python

import json
from datetime import datetime, timedelta
import textwrap
```
These import statements bring in the necessary modules for JSON handling, date and time operations, and text formatting

Load Habits Function
``` python

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
```
Loads the habits from the habits.json file.
Handles file not found and JSON decode errors gracefully.
Save Habits Function
``` python

def save_habits(habits):
    try:
        with open("habits.json", 'w') as file:
            json.dump(habits, file)
    except FileNotFoundError:
        error = print("File does not exist, check to see if it's loaded")
        return error
```
Saves the habits to the habits.json file.
Handles errors that may occur during the save process.
Add Habit Function
``` python

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
```
Adds a new habit to the list.
Validates input for non-empty and alphabetic characters.
Complete Habit Function
``` python

def complete_habit(habits):
    number = get_number(habits)
    if number is None:
        return
    habit = habits[number-1]
    habit['streak'] += 1
    print(habit['streak'])
```
Completes a habit by increasing its streak.
View Habits Function
``` python

def view_habits(habits):
    for habit in habits:
        print(f"name: {habit['name']}, streaks: {habit['streak']}, last update: {habit['modified_time']}")
```
Displays all habits with their names, streaks, and last update times.
Remove Habits Function
``` python

def remove_habits(habits):
    number = get_number(habits)
    if number is None:
        return
    del habits[number-1]
```
Removes a habit from the list by index.
Get Number Function
``` python

def get_number(habits):
    print("Habits: ")
    for i, habit in enumerate(habits, start=1):
        if 'name' in habit:
            print(f"{i}) {habit['name']}", end=', ')
    print()
    try:
        command = input("Enter the index of the habit you want to remove: ")
        if command == "":
            raise ValueError("Empty input")
        if not command.isdigit():
            raise ValueError("Input must be a number")
        number = int(command)
        if not 1 <= number <= len(habits):
            raise ValueError(f"Number must be between 1 and {len(habits)}")
    except ValueError as e:
        print(e)
        return None
    return number
```
Prompts the user to select a habit by index.
Validates the input.
Main Function
``` python

def main():
    while True:
        habits = load_habits()
        valid_inputs = ['1', '2', '3', '4', '5', 'q']
        command = input(" 1) Enter 1 for adding a habit \n 2) Enter 2 to add to your habit streak \n 3) Enter 3 to view current Habits \n 4) Enter 4 to remove a habit from the list \n 5) Enter 5 or q for quitting \n")
        if command in valid_inputs:
            if command == valid_inputs[0]:
                add_habit(habits)
            elif command == valid_inputs[1]:
                complete_habit(habits)
            elif command == valid_inputs[2]:
                view_habits(habits)
            elif command == valid_inputs[3]:
                remove_habits(habits)
            elif command in valid_inputs[-2:]:
                break
            save_habits(habits)
```
Main loop to handle user commands for adding, completing, viewing, and removing habits, or quitting the application.
### Run the Application
``` python

if __name__ == "__main__":
```
    main()
Entry point for the script. Runs the main function if the script is executed directly.
