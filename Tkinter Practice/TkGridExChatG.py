# ChatGPT generated.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sticky Demo")
root.geometry("300x150")

# Create a frame with padding
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Add 3 labels with background colors
label1 = tk.Label(mainframe, text="NW", bg="lightblue")
label2 = tk.Label(mainframe, text="Center", bg="lightgreen")
label3 = tk.Label(mainframe, text="Stretch", bg="salmon")

# Try different sticky values!
label1.grid(row=0, column=0, sticky="NW")         # Top-left corner
label2.grid(row=0, column=1, sticky="")           # Center (default)
label3.grid(row=1, column=0, columnspan=2, sticky="NSEW")  # Stretched across bottom

# Make the grid cells expand with the window
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

root.mainloop()
