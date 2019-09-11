import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Hello World")
# win.resizable(0,0)


def clickMe():
    action.configure(text="Hello " + name.get() + " " + number_selected.get())


# Adding Name label
name_label = ttk.Label(win, text="Enter a name:")
name_label.grid(column=0, row=0)

# Adding Name textfield
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=1, row=0)

# Adding button to click
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=0)
name_entered.focus()

# Adding Number label
number_label = ttk.Label(win, text="Choose a number:")
number_label.grid(column=0, row=1)

# Adding Number combobox
number = tk.StringVar()
number_selected = ttk.Combobox(
    win, width=12, textvariable=number, state="readonly")

# Adding number selection
number_selected['values'] = (1, 2, 3, 10, 20, 30)
number_selected.grid(column=1, row=1)
number_selected.current(0)

# Adding disabled button
disabled_button = ttk.Button(win, text="Disabled button!", command=clickMe)
disabled_button.grid(column=2, row=1)
disabled_button.configure(state="disabled")

# Adding checkbuttons states
checkbox_var_disabled = tk.IntVar()
checkbox_one = tk.Checkbutton(
    win, text="Disabled", variable=checkbox_var_disabled, state="disabled")
checkbox_one.select()
checkbox_one.grid(column=0, row=2, sticky=tk.W)

checkbox_var_unchecked = tk.IntVar()
checkbox_two = tk.Checkbutton(
    win, text="Unchecked", variable=checkbox_var_unchecked)
checkbox_two.deselect()
checkbox_two.grid(column=1, row=2, sticky=tk.W)

checkbox_var_enabled = tk.IntVar()
checkbox_three = tk.Checkbutton(
    win, text="Enabled", variable=checkbox_var_enabled)
checkbox_three.select()
checkbox_three.grid(column=2, row=2, sticky=tk.W)

# Adding radio buttons
COLOR_BLUE = "Blue"
COLOR_RED = "Red"
COLOR_YELLOW = "Yellow"


def selectRadioButton():
    radio_button_selection = radio_button_variable.get()
    if radio_button_selection == 1:
        win.configure(background=COLOR_BLUE)
    elif radio_button_selection == 2:
        win.configure(background=COLOR_RED)
    elif radio_button_selection == 3:
        win.configure(background=COLOR_YELLOW)


radio_button_variable = tk.IntVar()
radiobutton_one = tk.Radiobutton(
    win, text=COLOR_BLUE, variable=radio_button_variable, value=1, command=selectRadioButton)
radiobutton_one.grid(column=0, row=3, sticky=tk.W, columnspan=3)

radiobutton_two = tk.Radiobutton(
    win, text=COLOR_RED, variable=radio_button_variable, value=2, command=selectRadioButton)
radiobutton_two.grid(column=1, row=3, sticky=tk.W, columnspan=3)

radiobutton_three = tk.Radiobutton(
    win, text=COLOR_YELLOW, variable=radio_button_variable, value=3, command=selectRadioButton)
radiobutton_three.grid(column=2, row=3, sticky=tk.W, columnspan=3)

# Add scrolled text
scroll_w = 30
scroll_h = 3

scrolled_text = scrolledtext.ScrolledText(
    win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scrolled_text.grid(column=0, columnspan=3)

win.mainloop()
