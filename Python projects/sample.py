import tkinter as tk
from tkinter import simpledialog

def get_input():
    user_input = simpledialog.askstring("Input", "Enter your name:")
    if user_input:
        label.config(text="Hello, " + user_input + "!")

# Create the main application window
root = tk.Tk()
root.title("User Input Prompt")

# Create a label to display the greeting
label = tk.Label(root, text="Click the button to enter your name.")
label.pack(pady=10)

# Create a button to trigger the input prompt
button = tk.Button(root, text="Enter Name", command=get_input)
button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
