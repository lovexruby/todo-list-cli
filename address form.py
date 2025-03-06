import tkinter as tk
from tkinter import ttk
import json
import os
import numpy as np

FORM_FILE = "form_file" #Name the file


def save_form(form):
    with open(FORM_FILE, "w") as file_var:
        json.dump(form, file_var, indent = 4)

def clear_button_clicked():
    fnEntry.delete(0, tk.END)
    lnEntry.delete(0, tk.END)
    A1Entry.delete(0, tk.END)
    A2Entry.delete(0, tk.END)
    cityEntry.delete(0, tk.END)
    spEntry.delete(0, tk.END)
    pcEntry.delete(0, tk.END)
    countryEntry.delete(0, tk.END)

def submit_button_clicked():
    first_name = fnEntry.get()
    last_name = lnEntry.get()
    address1 = A1Entry.get()
    address2 = A2Entry.get()
    city = cityEntry.get()
    state_province = spEntry.get()
    postal_code = pcEntry.get()
    country = countryEntry.get()

    form = [
        {"first name": first_name},
        {"last name": last_name},
        {"address 1": address1},
        {"address 2": address2},
        {"city": city},
        {"state province": state_province},
        {"postal code": postal_code},
        {"country": country}
    ]

    save_form(form)
    json_file_path = os.path.abspath(FORM_FILE)
    os.system(f"pycharm {json_file_path}")

    #subprocess.run(["C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.4\bin\pycharm64.exe", json_file_path])

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
frame_main.columnconfigure([0,1,2], weight = 1)

labelFN = ttk.Label(master=frame_main, text = "First Name:")
fnEntry = ttk.Entry(master=frame_main)
labelLN = ttk.Label(master=frame_main, text = "Last Name:")
lnEntry = ttk.Entry(master=frame_main)
labelA1 = ttk.Label(master=frame_main, text = "Address 1:")
A1Entry = ttk.Entry(master=frame_main)
labelA2 = ttk.Label(master=frame_main, text = "Address 2:")
A2Entry = ttk.Entry(master=frame_main)
labelCity = ttk.Label(master=frame_main, text = "City:")
cityEntry = ttk.Entry(master=frame_main)
labelSP = ttk.Label(master=frame_main, text = "State/Province:")
spEntry = ttk.Entry(master=frame_main)
labelPC = ttk.Label(master=frame_main, text = "Postal Code:")
pcEntry = ttk.Entry(master=frame_main)
labelCountry = ttk.Label(master=frame_main, text = "Country:")
countryEntry = ttk.Entry(master=frame_main)


labelFN.grid(row=0, column=0, sticky = "e")
fnEntry.grid(row=0, column=1, sticky = "ew")
labelLN.grid(row=1, column=0, sticky = "e")
lnEntry.grid(row=1, column=1, sticky = "ew")
labelA1.grid(row=2, column=0, sticky = "e")
A1Entry.grid(row=2, column=1, sticky = "ew")
labelA2.grid(row=3, column=0, sticky = "e")
A2Entry.grid(row=3, column=1, sticky = "we")
labelCity.grid(row=4, column=0, sticky = "e")
cityEntry.grid(row=4, column=1, sticky = "ew")
labelSP.grid(row=5, column=0, sticky = "e")
spEntry.grid(row=5, column=1, sticky = "ew")
labelPC.grid(row=6, column=0, sticky = "e")
pcEntry.grid(row=6, column=1, sticky = "ew")
labelCountry.grid(row=7, column=0, sticky = "e")
countryEntry.grid(row=7, column=1, sticky = "ew")





clearButton = ttk.Button(frame_main,
                        text = "Clear",
                        command = clear_button_clicked)
submitButton = ttk.Button(frame_main,
                          text = "Submit",
                          command = submit_button_clicked)


clearButton.grid(row=8, column=1, columnspan=1, sticky = "w")
submitButton.grid(row = 8, column = 1, columnspan=1, sticky = "e")

button_decrease = ttk.Button(master=frame_main, text="-", command=decrease)
button_decrease.grid(row=9, column=0, sticky="nsew")

label_value_button = ttk.Label(master=frame_main, text="0")
label_value_button.grid(row=9, column=1)

button_increase = ttk.Button(master=frame_main, text="+", command=increase)
button_increase.grid(row=9, column=2, sticky="nsew")

button_roll = ttk.Button(master=frame_main, text="Roll the dice!", command=roll_dice)
button_roll.grid(row=0, column=2, rowspan=6, sticky="nsew")

label_value_dice = ttk.Label(master=frame_main, text="Roll your dice!")
label_value_dice.grid(row=6, column=2,rowspan=2)



window.mainloop()