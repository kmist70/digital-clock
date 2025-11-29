import tkinter as tk
from tkinter import font
import time

# updates the time every 1000 ms (1 second)
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    root.after(1000, update_time)    
    
# checks if the user input is a valid font color
def is_valid_color(root, color):
    try:
        root.winfo_rgb(color)
        return True
    except tk.TclError:
        return False

# main application window
print("Welcome to your Personalized Digital Clock!\n")

root = tk.Tk()
root.geometry("430x100")
root.title("Personalized Digital Clock")

# customizes font type, font color, and background color
all_fonts = set(font.families())
while True:
    user_font = input("Enter your preferred font (Make sure the first letter is capitalized) or press 'd' for default: ")
    if user_font in all_fonts:
        break
    elif user_font.lower() == 'd':
        user_font = "Arial"
        break
    else:
        print("Font not found. Please try again.")
        
        
while True:
    font_color = input("Enter your preferred font color as a word ('red') or as a hex ('#FF0000'), or press 'd' for default: ")
    if is_valid_color(root, font_color):
        break
    elif font_color.lower() == 'd':
        font_color = "white"
        break
    else:
        print("Invalid color. Please try again.")
        
while True:
    bg_color = input("Enter your preferred background color as a word ('blue') or as a hex ('#0000FF'), or press 'd' for default: ")
    if is_valid_color(root, bg_color):
        break
    elif bg_color.lower() == 'd':
        bg_color = "black"
        break
    else:
        print("Invalid color. Please try again.")


label = tk.Label(root, font=(user_font, 70), fg=font_color, bg=bg_color)
label.pack(padx=10, pady=10)

update_time()
root.mainloop()