import tkinter as tk

# Function to perform calculation
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operator.get()
    
    if operation == "+":
        result.set(num1 + num2)
    elif operation == "-":
        result.set(num1 - num2)
    elif operation == "*":
        result.set(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Divide by 0")

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")

# Entry fields
tk.Label(window, text="Enter first number:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Enter second number:").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Operator menu
tk.Label(window, text="Select operation:").pack()
operator = tk.StringVar(value="+")
tk.OptionMenu(window, operator, "+", "-", "*", "/").pack()

# Result display
result = tk.StringVar()
tk.Button(window, text="Calculate", command=calculate).pack(pady=10)
tk.Label(window, textvariable=result, font=("Arial", 16)).pack()

window.mainloop()
