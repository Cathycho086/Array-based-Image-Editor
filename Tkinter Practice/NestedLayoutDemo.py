# ChatGPT generated.
import tkinter as tk
from tkinter import ttk

# Set up the main window
root = tk.Tk()
root.title("Nested Layout Demo")
root.geometry("500x200")

# Create a colored frame (mainframe) inside root
mainframe = tk.Frame(root, bg="lightblue", padx=10, pady=10)
mainframe.grid(row=0, column=0, sticky="NSEW")

# Let root's only row and column expand with the window
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Add 3 buttons inside mainframe, all in row 0
btn1 = tk.Button(mainframe, text="A", bg="salmon")
btn2 = tk.Button(mainframe, text="B", bg="lightgreen")
btn3 = tk.Button(mainframe, text="C", bg="lightyellow")

btn1.grid(row=0, column=0, sticky="EW")
btn2.grid(row=0, column=1, sticky="EW")
btn3.grid(row=0, column=2, sticky="EW")

# Configure only column 1 of mainframe to grow
mainframe.columnconfigure(0, weight=0)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=0)

# Optional: add borders to show visual layout
mainframe.config(highlightbackground="black", highlightthickness=1)

# Now, let's add another frame directly into root to contrast
sidebar = tk.Frame(root, bg="gray", width=100)
sidebar.grid(row=0, column=1, sticky="NS")

# Configure root to allow the sidebar's column (1) to stay fixed,
# while the mainframe's column (0) takes extra width
root.columnconfigure(0, weight=3)  # mainframe gets more width
root.columnconfigure(1, weight=1)  # sidebar gets less

root.mainloop()
