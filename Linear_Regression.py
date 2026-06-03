import tkinter as tk
from tkinter import ttk, messagebox
import math


def calculate_regression():

    try:

        x_values = [float(x.strip())
                    for x in x_entry.get().split(",")]

        y_values = [float(y.strip())
                    for y in y_entry.get().split(",")]

        if len(x_values) != len(y_values):
            messagebox.showerror(
                "Error",
                "X and Y must contain same number of values"
            )
            return

        n = len(x_values)

        sum_x = sum(x_values)
        sum_y = sum(y_values)

        sum_xy = sum(x*y for x, y in zip(x_values, y_values))

        sum_x2 = sum(x*x for x in x_values)

        x_bar = sum_x / n
        y_bar = sum_y / n

        b = (
            (n * sum_xy) -
            (sum_x * sum_y)
        ) / (
            (n * sum_x2) -
            (sum_x ** 2)
        )

        a = y_bar - (b * x_bar)

        result_text.set(
            f"n = {n}\n\n"
            f"ΣX = {sum_x:.4f}\n"
            f"ΣY = {sum_y:.4f}\n"
            f"ΣXY = {sum_xy:.4f}\n"
            f"ΣX² = {sum_x2:.4f}\n\n"
            f"X̄ = {x_bar:.4f}\n"
            f"Ȳ = {y_bar:.4f}\n\n"
            f"b = {b:.4f}\n"
            f"a = {a:.4f}\n\n"
            f"Regression Equation:\n"
            f"Y = {a:.4f} + ({b:.4f})X"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            "Enter valid comma separated values"
        )


root = tk.Tk()
root.title("Linear Regression Calculator")
root.state("zoomed")
root.configure(bg="#f4f6f9")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Header.TLabel",
    font=("Segoe UI", 18, "bold")
)

style.configure(
    "TLabel",
    font=("Segoe UI", 11)
)

style.configure(
    "TButton",
    font=("Segoe UI", 11),
    padding=8
)


header = ttk.Label(
    root,
    text="Linear Regression Calculator",
    style="Header.TLabel"
)

header.pack(pady=20)


frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(
    frame,
    text="X Values (comma separated)"
).grid(row=0, column=0, padx=10, pady=10)

x_entry = ttk.Entry(frame, width=80)
x_entry.grid(row=0, column=1)

ttk.Label(
    frame,
    text="Y Values (comma separated)"
).grid(row=1, column=0, padx=10, pady=10)

y_entry = ttk.Entry(frame, width=80)
y_entry.grid(row=1, column=1)

tk.Button(
    root,
    text="Calculate Regression",
    command=calculate_regression,
    bg="#0078D7",      
    fg="white",        
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=8,
    cursor="hand2"
).pack(pady=20)


result_text = tk.StringVar()

result_label = ttk.Label(
    root,
    textvariable=result_text,
    font=("Segoe UI", 12),
    justify="left"
)

result_label.pack(pady=20)

root.mainloop()

# x = 11,13.5,13,12,15,14,14.5,13.5
# y = 75,65,62,76,50,58,54,64