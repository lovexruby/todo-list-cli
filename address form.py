import tkinter as tk
from tkinter import ttk
import json
import os


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

window = tk.Tk()

window.title("German Outdated Form")
window.minsize(300,200)

window.rowconfigure([0,1,2,3,4,5,6,7,8], weight = 1, minsize=10)
window.columnconfigure([0,1,2], weight = 1, minsize=0)


labelFN = ttk.Label(text = "First Name:")
fnEntry = ttk.Entry()
labelLN = ttk.Label(text = "Last Name:")
lnEntry = ttk.Entry()
labelA1 = ttk.Label(text = "Address 1:")
A1Entry = ttk.Entry()
labelA2 = ttk.Label(text = "Address 2:")
A2Entry = ttk.Entry()
labelCity = ttk.Label(text = "City:")
cityEntry = ttk.Entry()
labelSP = ttk.Label(text = "State/Province:")
spEntry = ttk.Entry()
labelPC = ttk.Label(text = "Postal Code:")
pcEntry = ttk.Entry()
labelCountry = ttk.Label(text = "Country:")
countryEntry = ttk.Entry()


labelFN.grid(row=0, column=0, sticky = "e")
fnEntry.grid(row=0, column=1, columnspan=2, sticky = "ew")
labelLN.grid(row=1, column=0, sticky = "e")
lnEntry.grid(row=1, column=1, columnspan=2, sticky = "ew")
labelA1.grid(row=2, column=0, sticky = "e")
A1Entry.grid(row=2, column=1, columnspan=2, sticky = "ew")
labelA2.grid(row=3, column=0, sticky = "e")
A2Entry.grid(row=3, column=1, columnspan=2, sticky = "we")
labelCity.grid(row=4, column=0, sticky = "e")
cityEntry.grid(row=4, column=1, columnspan=2, sticky = "ew")
labelSP.grid(row=5, column=0, sticky = "e")
spEntry.grid(row=5, column=1, columnspan=2, sticky = "ew")
labelPC.grid(row=6, column=0, sticky = "e")
pcEntry.grid(row=6, column=1, columnspan=2, sticky = "ew")
labelCountry.grid(row=7, column=0, sticky = "e")
countryEntry.grid(row=7, column=1, columnspan=2, sticky = "ew")





clearButton = ttk.Button(window,
                        text = "Clear",
                        command = clear_button_clicked)
submitButton = ttk.Button(window,
                          text = "Submit",
                          command = submit_button_clicked)





clearButton.grid(row=8, column=1, sticky = "ew")
submitButton.grid(row = 8, column = 2, sticky = "ew")






window.mainloop()