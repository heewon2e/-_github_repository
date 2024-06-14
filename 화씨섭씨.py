import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) / 1.8
        entry_celsius.delete(0, tk.END)
        entry_celsius.insert(0, f"{celsius:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for Fahrenheit.")

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 1.8) + 32
        entry_fahrenheit.delete(0, tk.END)
        entry_fahrenheit.insert(0, f"{fahrenheit:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for Celsius.")

def clear_fields():
    entry_fahrenheit.delete(0, tk.END)
    entry_celsius.delete(0, tk.END)

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Temperature Converter")

# Main frame
main_frame = tk.Frame(root)
main_frame.grid(padx=20, pady=20)

# Frame for Fahrenheit
frame_fahrenheit = tk.Frame(main_frame)
frame_fahrenheit.grid(row=0, column=0, padx=10, pady=10)

label_fahrenheit = tk.Label(frame_fahrenheit, text="Fahrenheit:")
label_fahrenheit.grid(row=0, column=0, padx=5, pady=5)

entry_fahrenheit = tk.Entry(frame_fahrenheit)
entry_fahrenheit.grid(row=0, column=1, padx=5, pady=5)

# Frame for Celsius
frame_celsius = tk.Frame(main_frame)
frame_celsius.grid(row=1, column=0, padx=10, pady=10)

label_celsius = tk.Label(frame_celsius, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=5, pady=5)

entry_celsius = tk.Entry(frame_celsius)
entry_celsius.grid(row=0, column=1, padx=5, pady=5)

# Frame for buttons
frame_buttons = tk.Frame(main_frame)
frame_buttons.grid(row=2, column=0, padx=10, pady=10)

button_f_to_c = tk.Button(frame_buttons, text="Fahrenheit -> Celsius", command=fahrenheit_to_celsius)
button_f_to_c.grid(row=0, column=0, columnspan=2, pady=5)

button_c_to_f = tk.Button(frame_buttons, text="Celsius -> Fahrenheit", command=celsius_to_fahrenheit)
button_c_to_f.grid(row=1, column=0, columnspan=2, pady=5)

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_fields)
button_clear.grid(row=2, column=0, padx=5, pady=5)

button_quit = tk.Button(frame_buttons, text="Quit", command=quit_program)
button_quit.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
