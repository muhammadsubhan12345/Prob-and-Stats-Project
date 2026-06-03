import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math
import numpy as np
import pandas as pd

z_table_df = pd.read_csv("ztable_stats.csv", sep=";")
z_table_df.rename(columns={z_table_df.columns[0]: "Z"}, inplace=True)
z_table_df.set_index("Z", inplace=True)

def normal_cdf(x, mean, std):
    z = (x - mean) / (std * math.sqrt(2))
    return 0.5 * (1 + math.erf(z))


def calculate():
    try:
        mean = float(mean_entry.get())
        std = float(std_entry.get())
        x = float(x_entry.get())

        if std <= 0:
            messagebox.showerror("Error", "Standard deviation must be > 0")
            return

        z = (x - mean) / std

        left_prob = normal_cdf(x, mean, std)
        right_prob = 1 - left_prob

        result_text.set(
            f"Z-Score = {z:.4f}\n"
            f"P(X < {x}) = {left_prob:.4f}\n"
            f"P(X > {x}) = {right_prob:.4f}"
        )

    except:
        messagebox.showerror("Error", "Enter valid values")


def z_table():
    try:
        mean = float(mean_entry.get())
        std = float(std_entry.get())
        x = float(x_entry.get())

        if std <= 0:
            messagebox.showerror("Error", "Standard deviation must be > 0")
            return

        z = (x - mean) / std

        z_row = round(z, 1)
        z_col = round((z - z_row), 2)

        col_name = f".{int(round(abs(z_col) * 100)):02d}"

        if z_row in z_table_df.index and col_name in z_table_df.columns:
            prob = float(z_table_df.loc[z_row, col_name])
        else:
            prob = None

        if prob is None:
            messagebox.showerror("Error", "Z value not found in table")
            return

        z_result.set(
            f"Z = {z:.4f}\n"
            f"Table Value = {prob:.4f}"
        )

    except:
        messagebox.showerror("Error", "Enter valid values")


root = tk.Tk()
root.title("Probability & Statistics")
root.geometry("700x600")
root.configure(bg="#f4f6f9")

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", font=("Segoe UI", 10))
style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))


header = ttk.Label(root, text="Normal Distribution", style="Header.TLabel")
header.pack(pady=15)


frame = ttk.Frame(root, padding=10)
frame.pack(pady=10)

ttk.Label(frame, text="Mean (μ)").grid(row=0, column=0, padx=5, pady=5)
mean_entry = ttk.Entry(frame, width=20)
mean_entry.grid(row=0, column=1)

ttk.Label(frame, text="Std Dev (σ)").grid(row=1, column=0, padx=5, pady=5)
std_entry = ttk.Entry(frame, width=20)
std_entry.grid(row=1, column=1)

ttk.Label(frame, text="Value (x)").grid(row=2, column=0, padx=5, pady=5)
x_entry = ttk.Entry(frame, width=20)
x_entry.grid(row=2, column=1)

btn_frame = ttk.Frame(root, padding=10)
btn_frame.pack()

tk.Button(btn_frame, text="Calculate Probability",
          command=calculate,
          bg="#4CAF50", fg="white",
          font=("Segoe UI", 10, "bold"),
          width=18).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="Z-Table",
          command=z_table,
          bg="#2196F3", fg="white",
          font=("Segoe UI", 10, "bold"),
          width=18).grid(row=0, column=2, padx=5, pady=5)

range_frame = ttk.Frame(root, padding=10)
range_frame.pack()

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Segoe UI", 11))
result_label.pack(pady=15)

z_result = tk.StringVar()
z_label = ttk.Label(root, textvariable=z_result, font=("Segoe UI", 11, "bold"))
z_label.pack(pady=10)

root.mainloop()