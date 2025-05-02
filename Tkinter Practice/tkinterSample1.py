# ChatGPT generated.
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Setting up the main application window.
root = Tk()
root.title("Feet to Meters")

# Creating a content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1) #-v
root.rowconfigure(0, weight=1) #----> tells Tk that frame should be expanded
                                    # to fill any extra space if window is resized.
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # parent:'mainframe'
feet_entry.grid(column=2, row=1, sticky=(W, E)) #place widget

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Polish->add padding so it isnt as cramped.
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus() #cursor will start in field 'feet_entry'
root.bind("<Return>", calculate)

root.mainloop() #Start the event loop.