from tkinter import *
from tkinter import ttk

# Setting up the main application window.
root = Tk()
root.title("sample")

def display(*args):
    try:
        display_text = str(input.get())
        display_text1.set(str(display_text))
    except ValueError:
        pass

# Creating a content frame.
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

#Stringvar(), Entry() demo
input = StringVar()
input_entry = ttk.Entry(mainframe, width=30, textvariable=input)
input_entry.grid(column=1, row=1, sticky=(W, E))

#Button() demo
ttk.Button(mainframe, text='It does smthing', command=display).grid(column=1, row=2)

#Displaying output demo
display_text1 = StringVar()
ttk.Label(mainframe, textvariable=display_text1, background='gray').grid(column=2, row=2)

#Label() demo
ttk.Label(mainframe, text='<-input input here!').grid(column=2, row=1, sticky=(W, E))

#some frills.
input_entry.focus()
root.bind("<Return>", display)

# Start the main loop.
root.mainloop()
