import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def calculate_Coeficient_correlation():
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
        sum_y2 = sum(y*y for y in y_values)

        r = (
            (n * sum_xy) - (sum_x * sum_y)
        ) / math.sqrt(         
            (n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)
        )

        global current_x_values, current_y_values, current_r
        current_x_values = x_values
        current_y_values = y_values
        current_r = r

        result_text.set(
            f"n = {n}\n\n"
            f"ΣX = {sum_x:.2f}\n"
            f"ΣY = {sum_y:.2f}\n"
            f"ΣXY = {sum_xy:.2f}\n"
            f"ΣX² = {sum_x2:.2f}\n\n"
            f"ΣY² = {sum_y2:.2f}\n\n"
            f"Correlation:\n"
            f"r = {r:.4f}\n"
            f"Status: {interpret_r(r)}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            "Enter valid comma separated values"
        )

def interpret_r(r):
    r_abs = abs(r)

    if r_abs >= 0.8:
        strength = "Strong"
    elif r_abs >= 0.5:
        strength = "Moderate"
    elif r_abs >= 0.2:
        strength = "Weak"
    else:
        strength = "Negligible"

    direction = "Positive" if r > 0 else "Negative" if r < 0 else "No"

    return f"{strength} Correlation"

def show_graph():
    try:
        if not current_x_values or not current_y_values:
            messagebox.showwarning(
                "Warning",
                "Please calculate correlation first before viewing graph"
            )
            return

        graph_window = tk.Toplevel(root)
        graph_window.title("Correlation Scatter Plot")
        graph_window.geometry("600x500")
        graph_window.configure(bg="#f4f6f9")

        fig, ax = plt.subplots(figsize=(6, 5), dpi=100)
        
        ax.scatter(current_x_values, current_y_values, color='blue', s=50, alpha=0.7, label='Data Points')
        
        z = np.polyfit(current_x_values, current_y_values, 1)
        p = np.poly1d(z)
        ax.plot(current_x_values, p(current_x_values), "r--", alpha=0.8, label=f'Trend Line (r={current_r:.3f})')
        
        ax.set_xlabel('X Values', fontsize=12, fontweight='bold')
        ax.set_ylabel('Y Values', fontsize=12, fontweight='bold')
        ax.set_title('Correlation Scatter Plot', fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        correlation_text = f"Correlation Coefficient (r) = {current_r:.4f}\n{interpret_r(current_r)}"
        ax.text(0.05, 0.95, correlation_text, transform=ax.transAxes, 
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        close_btn = tk.Button(
            graph_window,
            text="Close Graph",
            command=graph_window.destroy,
            bg="#0078D7",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            padx=15,
            pady=5,
            cursor="hand2"
        )
        close_btn.pack(pady=10)
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate graph: {str(e)}")

root = tk.Tk()
root.title("Correlation Calculator")
root.state("zoomed")
root.configure(bg="#f4f6f9")

current_x_values = []
current_y_values = []
current_r = 0

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
    text="Coefficient of Correlation Calculator",
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

button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=20)

calculate_btn = tk.Button(
    button_frame,
    text="Calculate Coefficient Correlation",
    command=calculate_Coeficient_correlation,
    bg="#0078D7",      
    fg="white",        
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=8,
    cursor="hand2"
)
calculate_btn.pack(side=tk.LEFT, padx=5)

graph_btn = tk.Button(
    button_frame,
    text="Graph",
    command=show_graph,
    bg="#4CAF50",      
    fg="white",        
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=8,
    cursor="hand2"
)
graph_btn.pack(side=tk.LEFT, padx=5)

result_text = tk.StringVar()

result_label = ttk.Label(
    root,
    textvariable=result_text,
    font=("Segoe UI", 12),
    justify="left"
)

result_label.pack(pady=20)

root.mainloop()


# x = 23,27,28,28,29,30,31,33,35,36
# y = 18,20,22,27,21,29,27,29,28,29     



# x = 66,77,22,11,55,90,32,44,10,19
# y = 18,20,22,27,21,29,27,29,28,29