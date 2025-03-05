import tkinter as tk

root = tk.Tk()
window = tk.Tk()

root.title("First Window")

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()


entry = tk.Entry()
entry.pack()

name = entry.get()
entry.delete(0)

def button_clicked():
    print("Button clicked!")

# Creating a button with specified options
button = tk.Button(root,
                   text="Click Me",
                   width=25,
                   height=5,
                   bg="blue",
                   fg="yellow",
                   )

#button.pack(padx=20, pady=20)



root.mainloop()

name = entry.get()
entry.delete(0)






border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}



for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()


frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)




for i in range(4):

    window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        window.columnconfigure(j, weight=1, minsize=70)
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=2
        )
        frame.grid(row=i, column=j, sticky="nsew")
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")







window.mainloop()