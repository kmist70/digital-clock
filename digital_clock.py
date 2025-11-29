import tkinter as tk
import time

# updates the time every 1000 ms (1 second)
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)


# main application window
root = tk.Tk()
root.title("Personalized Digital Clock")
label = tk.Label(root, font=("Helvetica", 48), fg="white", bg="black")
label.pack(padx=20, pady=20)

update_time()
root.mainloop()