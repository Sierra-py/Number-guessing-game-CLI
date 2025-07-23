#  importing required libraries.

import random
import tkinter as tk
from tkinter import messagebox

# Start message only for CLI

print('Welcome to the number guessing game')

# Defining some global variables.

max_range = 100                  #decides the range of number the computer can guess.
computer_no = random.randint(1, max_range)   #the number that computer guesses.
chances = 5                     # number of chances player gets. this variable is just initialised here, it will be changed inside function. 
user_no = None                  # initializing the variable that will store player's guess.
modes = ('easy', 'medium', 'hard')

# Creating the starting gui window

window = tk.Tk()
window.title("Number guessing game")
window.geometry("400x400")  # Width x Height

# The window that displays messages on the gui.
log = tk.Text(window,height='3', width= '50', state='disabled', wrap='word')
log.pack(side='bottom', pady=10)

def append_log(message):
    log.config(state='normal')
    log.insert(tk.END, message + '\n')
    log.config(state='disabled')
    log.see(tk.END)

# Choose Mode.

selected_mode = tk.StringVar() # creates a string variable which gets value from modes list and its default value is easy.
selected_mode.set(modes[0])
def mode_selection(): #fuction to get mode selected by user.
    global modes
    global chances
    user_mode = selected_mode.get()
    if user_mode == 'easy':
        chances = 5
    elif user_mode == 'medium':
        chances = 3
    elif user_mode == 'hard':
        chances = 1
    append_log(f"You selected: {user_mode}. You have {chances} chances.")
    
    if dropdown:
        dropdown.config(state=tk.DISABLED)
    if button_mode_selection:
        button_mode_selection.config(state=tk.DISABLED)
    if button_guess_number:
        button_guess_number.config(state=tk.ACTIVE)

dropdown = tk.OptionMenu(window, selected_mode, *modes) #creating a dropdown menu for selected_menu variable
dropdown.pack(pady=10)

button_mode_selection = tk.Button(window,text= 'Submit', command=mode_selection) # button that will trigger the mode_selection function.
button_mode_selection.pack(pady=10)

#  Main function that matches the user number with the computer number

guess = tk.Entry(window) #creating input field that takes input from player.
guess.pack()
def match():
    global chances 
    global max_range
    global user_no
    try:
        user_no = int(guess.get())
    except ValueError:
        append_log("Please input valid number")
    if user_no < 1 or user_no > max_range:
        append_log('Please enter valid number')
        
    elif user_no != computer_no:
        if computer_no > user_no:
            append_log(f"\nIncorect. Number is greater than {user_no}")
        else:
            append_log(f'\nIncorrect. Number is less than: {user_no}')
        chances -= 1
     
    elif user_no == computer_no:
        append_log('Congratulations! You win.')
        chances = 0
    

    if chances == 0 and user_no != computer_no:
        append_log(f"Chances over.\nYou lose. The number was: {computer_no}")
        button_guess_number.config(state=tk.DISABLED)
    guess.delete(0, tk.END)

button_guess_number = tk.Button(window,text= 'Comfirm', command=match, state=tk.DISABLED) # button to trigger the main function
button_guess_number.pack(pady=10)

window.bind('<Return>', lambda event: button_guess_number.invoke())  #pressing enter button will invoke button_guess_number 
button_guess_number.focus_set()

# adding a reset function.
def reset_game():
    global computer_no
    computer_no = random.randint(1,10)
    guess.delete(0, tk.END)
    if dropdown:
        dropdown.config(state=tk.NORMAL)
    if button_mode_selection:
        button_mode_selection.config(state=tk.NORMAL)
    if button_guess_number:
        button_guess_number.config(state="disabled")
    return computer_no
    

reset_button = tk.Button(window, text='Restart Game', command= reset_game)  # a button that will trigger the reset function.
reset_button.pack(pady=10)

# adding a button to close the game

close_button = tk.Button(window, text= 'Exit game', command= window.destroy)
close_button.pack(pady=10)

window.mainloop()