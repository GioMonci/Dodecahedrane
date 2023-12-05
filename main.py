import tkinter as tk
from tkinter import ttk

# Window init
window = tk.Tk()
window.title("Fluoroantimonic")
window.geometry("1280x720")

# Title --> Label is another word for text
title_label = ttk.Label(master=window, text="Fluoroantimonic", font="Arial 24 bold")
# Display title
title_label.pack()

# Input Field

# Frame widget used to organized other widgets, think of it as a container
# Window is the Master because it is the parent widget
input_frame = ttk.Frame(master=window)

# Where they are going to put in the input
# input_frame is master because entry is inside the frame container
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text="Meat", command='')
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(padx=10)

# Output
output_label = ttk.Label(master=window, text='Output', font="Arial 24")
output_label.pack(pady=5)

def main_logic():
    print("Hello World")
    print("Button Working")
# Run
window.mainloop()
