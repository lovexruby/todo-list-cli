import tkinter as tk
from tkinter import ttk
import json
import os
import subprocess


FORM_FILE = "form_file"


def save_form(form):
    with open(FORM_FILE, "w") as file:
        json.dump(form, file, indent = 4)

def clearButton_clicked():
    fnEntry.delete(0, tk.END)
    lnEntry.delete(0, tk.END)
    A1Entry.delete(0, tk.END)
    A2Entry.delete(0, tk.END)
    cityEntry.delete(0, tk.END)
    spEntry.delete(0, tk.END)
    pcEntry.delete(0, tk.END)
    countryEntry.delete(0, tk.END)



def submitButton_clicked():
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
    #os.system(f"pycharm {json_file_path}")

    subprocess.run(["C:\Program Files\JetBrains\PyCharm Community Edition 2024.3.4\bin\pycharm64.exe", json_file_path])

window = tk.Tk()

window.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=10)
window.columnconfigure([0,1,2], minsize=0)


labelFN = tk.Label(text = "First Name:")
fnEntry = tk.Entry()
labelLN = tk.Label(text = "Last Name:")
lnEntry = tk.Entry()
labelA1 = tk.Label(text = "Address 1:")
A1Entry = tk.Entry()
labelA2 = tk.Label(text = "Address 2:")
A2Entry = tk.Entry()
labelCity = tk.Label(text = "City:")
cityEntry = tk.Entry()
labelSP = tk.Label(text = "State/Province:")
spEntry = tk.Entry()
labelPC = tk.Label(text = "Postal Code:")
pcEntry = tk.Entry()
labelCountry = tk.Label(text = "Country:")
countryEntry = tk.Entry()



labelFN.grid(row=0, column=0, sticky = "e")
fnEntry.grid(row=0, column=1, columnspan=2)
labelLN.grid(row=1, column=0, sticky = "e")
lnEntry.grid(row=1, column=1, columnspan=2)
labelA1.grid(row=2, column=0, sticky = "e")
A1Entry.grid(row=2, column=1, columnspan=2)
labelA2.grid(row=3, column=0, sticky = "e")
A2Entry.grid(row=3, column=1, columnspan=2)
labelCity.grid(row=4, column=0, sticky = "e")
cityEntry.grid(row=4, column=1, columnspan=2)
labelSP.grid(row=5, column=0, sticky = "e")
spEntry.grid(row=5, column=1, columnspan=2)
labelPC.grid(row=6, column=0, sticky = "e")
pcEntry.grid(row=6, column=1, columnspan=2)
labelCountry.grid(row=7, column=0, sticky = "e")
countryEntry.grid(row=7, column=1, columnspan=2)





clearButton = tk.Button(window,
                        text = "Clear",
                        command = clearButton_clicked)
submitButton = ttk.Button(window,
                          text = "Submit",
                          command = submitButton_clicked)





clearButton.grid(row=8, column=1)
submitButton.grid(row = 8, column = 2)






window.mainloop()