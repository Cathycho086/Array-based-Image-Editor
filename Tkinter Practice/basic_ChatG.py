import tkinter as tk

def say_hello():
    print("Hello!")

# Create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

# Create a button
button = tk.Button(root, text="Click Me!", command=say_hello)
button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
