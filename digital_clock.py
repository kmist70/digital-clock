import tkinter as tk
from tkinter import font
import time

# updates the time every 1000 ms (1 second)
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    root.after(1000, update_time)
    
# checks if the user input is a valid color
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

# lists available fonts
all_fonts = sorted(font.families())
print("Available fonts:")
for f in all_fonts: print(" -", f)

# customizes font type
font_map = {f.lower(): f for f in font.families()}

while True:
    user_font = input("\nEnter your preferred font or press 'd' for default: ")
    if user_font.lower() == 'd':
        user_font = "Arial"
        break
    lf = user_font.lower()
    if lf in font_map:
        user_font = font_map[lf]
        break
    else:
        print("Font not found. Please try again.")
        
# asks if user wants pre-made or custom themes
while True:
    theme_choice = input("\nWould you like to use a pre-made theme? (y/n): ").lower()
    if theme_choice in ['y', 'n']:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
if theme_choice == 'y':
    print("\nAvailable themes:")
    print("- Light")
    print("- Dark")
    print("- Sunny")
    while True:
        theme = input("\nChoose a theme: ").lower()
        if theme in ["dark", "light", "sunny"]:
            break
        else:
            print("Invalid choice. Please enter one of the listed themes.")
    
    # applies pre-made themes
    if theme == "dark":
        font_color = "white"
        bg_color = "black"
    elif theme == "light":
        font_color = "black"
        bg_color = "white"
    elif theme == "sunny":
        font_color = "yellow"
        bg_color = "blue"
else:
    # customizes font color and background color
    while True:
        font_color = input("\nEnter your preferred font color as a word ('red') or as a hex ('#FF0000'), or press 'd' for default: ")
        if is_valid_color(root, font_color):
            break
        elif font_color.lower() == 'd':
            font_color = "white"
            break
        else:
            print("Invalid color. Please try again.")
            
    while True:
        bg_color = input("\nEnter your preferred background color as a word ('blue') or as a hex ('#0000FF'), or press 'd' for default: ")
        if is_valid_color(root, bg_color):
            break
        elif bg_color.lower() == 'd':
            bg_color = "black"
            break
        else:
            print("Invalid color. Please try again.")

# apply user preferences
label = tk.Label(root, font=(user_font, 70), fg=font_color, bg=bg_color)
label.pack(padx=10, pady=10)
print("Your personalized digital clock is now running!")

update_time()
root.mainloop()