import tkinter as tk
from tkinter import ttk
import json
import numpy as np

#initiating the variables
FORM_FILE = "form_file" #name the file
entries = {}            #initiate entries dictionary
labels = ["First Name:", "Last Name:", "Address 1:", "Address 2:", "City:", "State/Province:", "Postal Code:", "Country:"]#initiate the labels for the form
###################
def save_form():    #function to save the input forms
    form = {label_val: entry_val.get() for label_val, entry_val in entries.items()} #variable to save the input of the form entries
    with open(FORM_FILE, "w") as file_var:      #open the file (if existing, else create it)
        json.dump(form, file_var, indent = 4)   #save the form in a separate file

def clear_button_clicked():         #function to clear all the input entries out of the form
    for entry_val in entries.values():  #for-loop to go through all the entry fields
        entry_val.delete(0, tk.END) #delete each of the entry fields

def increase(): #funtion to increase the counter
    value = int(label_value_button["text"]) #counter variable
    label_value_button["text"] = f"{value + 1}" #increase counter variable by one

def decrease(): #function to decrease the counter
    value = int(label_value_button["text"]) #counter variable
    label_value_button["text"] = f"{value - 1}" #decrease the counter by one

def roll_dice():    #function to generate a random dice number
    value = np.random.randint(1, 7) #variable that generates a random number between 1-6
    label_value_dice["text"] =f"{value}"    #save and print the random variable in the label

def convert_fh_c():     #function to convert Fahrenheit input into Celsius
    fahrenheit = fh_entry.get()     #load the input Fahrenheit from entry
    celsius = (5 / 9) * (float(fahrenheit) - 32)    #convert mathematically
    cel_label["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"   #save and print Celsius variable in the label
######################
window = tk.Tk()        #initialize the tkinter window

#window parameters
window.title("German Outdated Form")    #window title
window.minsize(490,200)     #window minimum size in pixels

#configuration of window in resizable rows and columns
window.rowconfigure([0], weight = 1)    #rowconfiguration
window.columnconfigure([0], weight = 1) #columnconfiguration

#frame parameters
frame_main = tk.Frame(master=window, borderwidth=5, relief=tk.GROOVE)   #initiating the main frame
frame_main.grid(row=0, column=0, sticky="nsew") #positioning main frame

#configuration of frame in resizable rows and columns
frame_main.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight = 1)  #rowconfiguration
frame_main.columnconfigure([0,1,2, 3], weight = 1)          #columnconfiguration

#loop to create the entries and their respective labels from the labels dictionary
for lID, lText in enumerate(labels):
    label = ttk.Label(master=frame_main, text=lText)    #create label
    entry = ttk.Entry(master=frame_main)                #create entry
    label.grid(row = lID, column= 0, sticky="e")        #position label in grid
    entry.grid(row=lID, column=1, sticky="ew")          #position entry in grid

    entries[lText] = entry                              #saving the input entries in a list
#creating clear and submit buttons for the address form
clearButton = ttk.Button(frame_main, text = "Clear", command = clear_button_clicked)    #button to clear form
clearButton.grid(row=8, column=1, sticky = "w")         #position clear button
submitButton = ttk.Button(frame_main, text = "Submit", command = save_form)             #button to submit form
submitButton.grid(row = 8, column = 1,  sticky = "e")   #position submit form

#creating labels, entry and button for Fahrenheit to Celsius converter
conv_label = ttk.Label(master=frame_main, text="Convert Fahrenheit to Celsius! \N{DOWNWARDS BLACK ARROW}")  #converting label
conv_label.grid(row=6, column=2, columnspan=2)  #position converting label in grid
fh_entry = ttk.Entry(master=frame_main)         #entry to input Fahrenheit integer
fh_entry.grid(row=7, column=2, sticky="ew")     #position Fahrenheit entry in grid
fh_label = ttk.Label(master=frame_main, text="\N{DEGREE FAHRENHEIT}")   #Fahrenheit sign label
fh_label.grid(row=7, column=3, sticky="e")                              #position Fahrenheit label in grid
conv_button = ttk.Button(frame_main, text="\N{RIGHTWARDS BLACK ARROW}", command= convert_fh_c)  #button to convert from Fahrenheit to Celsius
conv_button.grid(row=8, column=2, sticky="ew")  #position Button in grid
cel_label = ttk.Label(master=frame_main,text="\N{DEGREE CELSIUS}")  #Celsius sign label
cel_label.grid(row=8, column=3, sticky="e")     #position Celsius label in grid

#creating button and label for random roll dice
button_roll = ttk.Button(master=frame_main, text="Roll the dice!", command=roll_dice)           #creating button to generate random dice number
button_roll.grid(row=0, column=2, rowspan=4, columnspan=2, sticky="nsew")                       #position random button in grid
label_value_dice = ttk.Label(master=frame_main, text="Roll your dice! \N{UPWARDS BLACK ARROW}") #label to display the random dice number
label_value_dice.grid(row=4, column=2,columnspan=2, rowspan=2)                                  #position label in grid

#creating buttons and label to change number counter
button_decrease = ttk.Button(master=frame_main, text="-", command=decrease) #button to decrease the counter by one
button_decrease.grid(row=9, column=0, sticky="nsew")                        #position button in grid
label_value_button = ttk.Label(master=frame_main, text="0")                 #label to display the counter number
label_value_button.grid(row=9, column=1)                                    #position label in grid
button_increase = ttk.Button(master=frame_main, text="+", command=increase) ##button to decrease the counter by one
button_increase.grid(row=9, column=2, sticky="nsew")          #position button in grid


window.mainloop()