"""
# I have shown some of my code to a contact at Optimizely (a company I am interested in working for)
# He said that I need to work on documenting more in my projects
#  I will be practicing documentation more this module and my final please give me any you are willing to!
Brandon Treu 900704435
numberGuessingGUI.py
Number Guessing Game with min to max numbers played via GUI
"""
#  import GUI framework
import tkinter as tk
import random

# GUI window creation
window = tk.Tk()

# GUI window dimension
window.geometry("600x400")

# GUI window background color
window.config(bg="#065569")
#  make GUI unable to resize
window.resizable(width=False, height=False)

# Window TITLE
window.title('Guessing Game')

# sets number to be guessed and retries init
TARGET = random.randint(0, 100)
RETRIES = 0


def update_result(text):  # updates the user results
    result.configure(text=text)


def new_game():  # starts new game
    guess_button.config(state='normal')
    global TARGET, RETRIES
    TARGET = random.randint(0, 1000)
    RETRIES = 0
    update_result(text="Guess a number between\n 1 and 100")


def play_game():  # this will continue the ongoing game
    global RETRIES

    choice = int(number_form.get())

    if choice != TARGET:
        RETRIES += 1

        result = "Wrong Guess!! Try Again"
        if TARGET < choice:
            hint = "number lies between 0 and {}".format(result)
        else:
            hint = "number lies between {} and 100".format(choice)
        result += "\n\nHINT :\n" + hint

    else:
        result = "You guessed the correct number after {} retries".format(RETRIES)
        guess_button.configure(state='disabled')
        result += "\n" + "Click on Play to start a new game"

    update_result(result)


# Heading of our game
title = tk.Label(window, text="Guessing Game", font=("Arial", 24), fg="#fffcbd", bg="#065569")

# Result and hints of our game
result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"), fg="White",
                  bg="#065569", justify=tk.LEFT)

# Play Button
play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                        command=new_game)

# Guess Button
guess_button = tk.Button(window, text="Guess", font=("Arial", 13), state='disabled', fg="#13d675", bg="Black",
                         command=play_game)

# Exit Button
exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=exit)

# Entry Fields
guessed_number = tk.StringVar()
number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

# Place the labels

title.place(x=170, y=50)
result.place(x=180, y=210)

# Place the buttons
exit_button.place(x=300, y=320)
guess_button.place(x=350, y=147)
play_button.place(x=170, y=320)

# Place the entry field
number_form.place(x=180, y=150)

# Start the window
window.mainloop()