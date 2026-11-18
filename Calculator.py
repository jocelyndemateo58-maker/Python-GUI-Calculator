import re
import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("380x550")
window.resizable(False, False)
window.configure(bg="#141820")


expression = ""


display = tk.Entry(
    window,
    font=("Segoe UI", 28, "bold"),
    bg="#222834",
    fg="#f8fafc",
    insertbackground="#38bdf8",
    justify="right",
    bd=0,
)
display.pack(fill="x", padx=16, pady=20, ipady=22)



def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace",
        "Delete",
        "Left",
        "Right",
    ):
        return None
    return "break"



def sync_expression(event):
    global expression
    expression = display.get()



display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)



def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)



def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)



def clear_entry():
    global expression
    expression = re.sub(r"[0-9.]+$", "", expression)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)



def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)



def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""



buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"],
]


button_frame = tk.Frame(window, bg="#141820")
button_frame.pack(expand=True, fill="both", padx=12, pady=8)


clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Segoe UI", 20, "bold"),
    bg="#e11d48",
    fg="white",
    bd=0,
    command=clear,
)
clear_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


ce_button = tk.Button(
    button_frame,
    text="CE",
    font=("Segoe UI", 20, "bold"),
    bg="#7c3aed",
    fg="white",
    bd=0,
    command=clear_entry,
)
ce_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


backspace_button = tk.Button(
    button_frame,
    text="⌫",
    font=("Segoe UI", 20, "bold"),
    bg="#334155",
    fg="#f8fafc",
    bd=0,
    command=backspace,
)
backspace_button.grid(
    row=0, column=2, columnspan=2, sticky="nsew", padx=5, pady=5
)


for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):
        if value == "=":
            command = calculate
            color = "#10b981"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#f59e0b"
        else:
            command = lambda v=value: button_click(v)
            color = "#28303f"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Segoe UI", 20, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command,
        )
        button.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)


window.mainloop()