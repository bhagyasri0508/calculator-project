Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import tkinter as tk
from tkinter import ttk, messagebox
import math
import calendar
from datetime import datetime

# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Advanced Scientific Calculator + Calendar")
root.geometry("650x700")
root.config(bg="#1e1e1e")

expression = ""

# ---------------- FUNCTIONS ---------------- #
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def scientific(func):
    global expression
    try:
        value = eval(expression)

        operations = {
            'sin': math.sin(math.radians(value)),
            'cos': math.cos(math.radians(value)),
            'tan': math.tan(math.radians(value)),
            'sqrt': math.sqrt(value),
            'log': math.log10(value),
            'ln': math.log(value),
            'fact': math.factorial(int(value)),
            'square': value ** 2,
            'cube': value ** 3
        }

        result = operations.get(func, "Error")

        equation.set(str(result))
        expression = str(result)

    except:
        equation.set("Error")
        expression = ""

# ---------------- CALENDAR FUNCTION ---------------- #
def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        cal = calendar.month(year, month)

        calendar_window = tk.Toplevel(root)
        calendar_window.title("Calendar")
        calendar_window.geometry("400x300")

        text = tk.Text(calendar_window, font=("Courier", 14))
        text.pack(expand=True, fill="both")

        text.insert(tk.END, cal)

    except:
        messagebox.showerror("Error", "Enter valid month and year")

# ---------------- DISPLAY ---------------- #
equation = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify='right',
    bg="white"
)

entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# ---------------- BUTTON FRAME ---------------- #
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

buttons = [
    ['7', '8', '9', '/', 'sqrt'],
    ['4', '5', '6', '*', 'square'],
    ['1', '2', '3', '-', 'cube'],
    ['0', '.', '=', '+', 'clear'],
    ['sin', 'cos', 'tan', 'log', 'ln'],
    ['fact', '(', ')']
]

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill='both')

    for btn in row:
        action = lambda x=btn: (
            clear() if x == 'clear'
            else equal() if x == '='
            else scientific(x) if x in
            ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'fact', 'square', 'cube']
            else press(x)
        )

        tk.Button(
            row_frame,
            text=btn,
            command=action,
            font=("Arial", 16),
            width=8,
            height=2,
            bg="#2d2d2d",
            fg="white",
            activebackground="#00adb5"
        ).pack(side='left', expand=True, fill='both', padx=2, pady=2)

# ---------------- CALENDAR SECTION ---------------- #
calendar_frame = tk.LabelFrame(
    root,
...     text="Calendar",
...     font=("Arial", 14),
...     bg="#1e1e1e",
...     fg="white"
... )
... 
... calendar_frame.pack(fill="both", padx=10, pady=10)
... 
... tk.Label(calendar_frame, text="Year", bg="#1e1e1e", fg="white").grid(row=0, column=0, padx=5, pady=5)
... year_entry = tk.Entry(calendar_frame)
... year_entry.grid(row=0, column=1)
... 
... tk.Label(calendar_frame, text="Month", bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=5, pady=5)
... month_entry = tk.Entry(calendar_frame)
... month_entry.grid(row=1, column=1)
... 
... tk.Button(
...     calendar_frame,
...     text="Show Calendar",
...     command=show_calendar,
...     bg="#00adb5",
...     fg="white",
...     font=("Arial", 12)
... ).grid(row=2, column=0, columnspan=2, pady=10)
... 
... # ---------------- FOOTER ---------------- #
... footer = tk.Label(
...     root,
...     text=f"Today: {datetime.now().strftime('%d-%m-%Y')}",
...     bg="#1e1e1e",
...     fg="lightgreen",
...     font=("Arial", 12)
... )
... 
... footer.pack(pady=10)
... 
... # ---------------- RUN ---------------- #
