import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        option = int(entry_option.get())

        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2
        elif option == 3:
            result = num1 * num2
        elif option == 4:
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid option. Please enter 1, 2, 3, or 4.")
            return

        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

label_option = tk.Label(root, text="Enter option (1:Add, 2:Subtract, 3:Multiply, 4:Divide):")
label_option.grid(row=2, column=0)
entry_option = tk.Entry(root)
entry_option.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
