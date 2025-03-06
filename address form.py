import tkinter as tk
from tkinter import ttk
import json
import os
import numpy as np

FORM_FILE = "form_file" #Name the file
entries = {}

def save_form(form):
    with open(FORM_FILE, "w") as file_var:
        json.dump(form, file_var, indent = 4)

def clear_button_clicked():
    for entry in entries.values():
        entry.delete(0, tk.END)

def submit_button_clicked():
    form = {label: entry.get() for label, entry in entries.items()}
    print(form)
    save_form(form)

def increase():
    value = int(label_value_button["text"])
    label_value_button["text"] = f"{value + 1}"

def decrease():
    value = int(label_value_button["text"])
    label_value_button["text"] = f"{value - 1}"

def roll_dice():
    value = np.random.randint(1, 7)
    label_value_dice["text"] =f"{value}"

window = tk.Tk()

window.title("German Outdated Form")
window.minsize(365,200)

window.rowconfigure([0], weight = 1)
window.columnconfigure([0], weight = 1)

frame_main = tk.Frame(master=window, borderwidth=5, relief=tk.GROOVE)
frame_main.grid(row=0, column=0, sticky="nsew")

frame_main.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight = 1)
frame_main.columnconfigure([0,1,2, 3], weight = 1)

labels = ["First Name:", "Last Name:", "Address 1:", "Address 2:", "City:", "State/Province:", "Postal Code:", "Country:"]

for lID, lText in enumerate(labels):
    label = ttk.Label(master=frame_main, text=lText)
    entry = ttk.Entry(master=frame_main)
    label.grid(row = lID, column= 0, sticky="e")
    entry.grid(row=lID, column=1, sticky="ew")

    entries[lText] = entry


def convert_fh_c():
    fahrenheit = fh_entry.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    cel_label["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


conv_label = ttk.Label(master=frame_main, text="Convert Fahrenheit to Celsius! \N{DOWNWARDS BLACK ARROW}")
fh_entry = ttk.Entry(master=frame_main)
fh_label = ttk.Label(master=frame_main, text="\N{DEGREE FAHRENHEIT}")
conv_button = ttk.Button(frame_main,
                         text="\N{RIGHTWARDS BLACK ARROW}",
                         command= convert_fh_c)
cel_label = ttk.Label(master=frame_main,text="\N{DEGREE CELSIUS}")


conv_label.grid(row=6, column=2, columnspan=2)
fh_entry.grid(row=7, column=2, sticky="ew")
fh_label.grid(row=7, column=3, sticky="e")
conv_button.grid(row=8, column=2, sticky="ew")
cel_label.grid(row=8, column=3, sticky="e")

clearButton = ttk.Button(frame_main,
                        text = "Clear",
                        command = clear_button_clicked
                        )
submitButton = ttk.Button(frame_main,
                          text = "Submit",
                          command = submit_button_clicked
                          )

clearButton.grid(row=8, column=1, sticky = "w")
submitButton.grid(row = 8, column = 1,  sticky = "e")

button_decrease = ttk.Button(master=frame_main, text="-", command=decrease)
button_decrease.grid(row=9, column=0, sticky="nsew")

label_value_button = ttk.Label(master=frame_main, text="0")
label_value_button.grid(row=9, column=1)

button_increase = ttk.Button(master=frame_main, text="+", command=increase)
button_increase.grid(row=9, column=2, columnspan=2, sticky="nsew")

button_roll = ttk.Button(master=frame_main, text="Roll the dice!", command=roll_dice)
button_roll.grid(row=0, column=2, rowspan=4, columnspan=2, sticky="nsew")

label_value_dice = ttk.Label(master=frame_main, text="Roll your dice! \N{UPWARDS BLACK ARROW}")
label_value_dice.grid(row=4, column=2,columnspan=2, rowspan=2)



window.mainloop()