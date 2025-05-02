# ChatGPT generated.
import tkinter as tk
from tkinter import ttk

# Main application window
root = tk.Tk()
root.title("Column Weight Example")
root.geometry("400x100")

# Create a frame to hold widgets
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky="NSEW")

# Configure root so that its row/column allows the frame to grow
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Add three buttons into the frame
ttk.Button(mainframe, text="Button 1").grid(row=0, column=0, sticky="EW")
ttk.Button(mainframe, text="Button 2").grid(row=0, column=1, sticky="EW")
ttk.Button(mainframe, text="Button 3").grid(row=0, column=2, sticky="EW")

# Only column 1 grows when resized
mainframe.columnconfigure(0, weight=0)
mainframe.columnconfigure(1, weight=1)  # This one grows!
mainframe.columnconfigure(2, weight=0)

# You can also allow the row to expand
mainframe.rowconfigure(0, weight=1)

root.mainloop()
