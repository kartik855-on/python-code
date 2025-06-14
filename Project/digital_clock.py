import tkinter as tk
from time import strftime

# Create window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x100")
window.configure(bg="black")

# Clock label
label = tk.Label(window, font=("Arial", 40, "bold"), background="black", foreground="cyan")
label.pack(anchor="center")

# Update time function
def update_time():
    time_string = strftime("%H:%M:%S %p")  # Format: Hour:Minute:Second AM/PM
    label.config(text=time_string)
    label.after(1000, update_time)  # Update every 1000ms (1 second)

update_time()
window.mainloop()
