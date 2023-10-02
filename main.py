import random
import string
import tkinter as tk
from tkinter import ttk

def close():
    root.destroy()
def generate_password():
    length = int(length_entry.get())

    letters = string.ascii_letters
    digits = string.digits
    special_characters = "!@#$%^&*()_-+=<>?/[]{}|"
    all_characters = letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(length))

    result_label.config(text="Generated Password: " + password)


# Create a GUI window
root = tk.Tk()
root.title("Password Generator")

# Change the background color of the main window
root.configure(bg="light gray")  # Set the desired background color here

# Create and configure GUI elements
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

length_entry = ttk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)


generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=0, column=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)


close_button = ttk.Button(root, text="Close", command=close)
close_button.grid(row=2, column=0,columnspan=3, padx=10, pady=10)


# Center the elements vertically and horizontally
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the GUI event loop
root.mainloop()
