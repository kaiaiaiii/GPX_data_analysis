##What to do as a user
## resolution of heightmap
## number of plots
import tkinter as tk

window = tk.Tk()
window.title("GPX Data Analysis")

def get_entry_value_resolution():
    resolution = entry.get()
    return resolution

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Get Entry Value", command=get_entry_value)
button.pack()

window.mainloop()