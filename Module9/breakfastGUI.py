import tkinter
"""
Brandon Treu 900704435
Creates tkinter GUI to pick your favorite meal. 
Press Action buttons to change text
Press the exit button to destroy GUI
"""


def breakfastFunct():
    label.config(text="You've already had breakfast!")

def secondBreakfast():
    label.config(text="Aye, but what about second breakfast?")


m = tkinter.Tk()
m.title("Favorite Meal")
label = tkinter.Label(m, text="Waiting for your selection")
label.grid(row=5)

var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=breakfastFunct).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=secondBreakfast).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=breakfastFunct).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=breakfastFunct).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)  # exit this way
exit_button.grid(row=6)
m.mainloop()