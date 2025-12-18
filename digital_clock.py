import tkinter as tk
from tkinter import font
import time

# updates the time every 1000 ms (1 second)
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    label.config(text=current_time)
    root.after(1000, update_time)

# checks if the font input is valid with a provided function
def get_valid_font(font_map):
    user_input = input("\nEnter your preferred font or press 'd' for default: ")
    if user_input.lower() == 'd':
        return "Arial"
    
    result = font_map.get(user_input.lower())
    if result:
        return result
        
    print("Font not found. Please try again.")

# checks if the theme input is valid with a provided function
def get_valid_theme(theme_map):
    user_input = input("\nChoose a theme: ").lower()
    result = theme_map.get(user_input)
    if result:
        return result

    print("Invalid choice. Please enter one of the listed themes.")

# helper function for picking fg and bg colors
def choose_color(prompt, default):
    user_input = input(prompt)
    if user_input.lower() == 'd':
        return default
    elif is_valid_color(root, user_input):
        return user_input
    else:
        print("Invalid color. Please try again.")

# checks if the user input is a valid color
def is_valid_color(root, color):
    try:
        root.winfo_rgb(color)
        return True
    except tk.TclError:
        return False
        
# ------------------------------------------------------------------------
# main application window
print("Welcome to your Personalized Digital Clock!\n")

root = tk.Tk()
root.withdraw()  # hides the window while setting up the clock
root.geometry("430x100")
root.title("Personalized Digital Clock")

# lists available fonts
all_fonts = sorted(font.families())
print("Available fonts:")
for f in all_fonts: print(" -", f)

# customizes font type
font_map = {f.lower(): f for f in font.families()}
user_font = None
while user_font is None:
    user_font = get_valid_font(font_map)
            
# asks if user wants pre-made or custom themes
themes = {
    "dark": {"font_color": "white", "bg_color": "black"},
    "light": {"font_color": "black", "bg_color": "white"},
    "sunny": {"font_color": "yellow", "bg_color": "blue"}
}
while True:
    wants_themes = input("\nWould you like to use a pre-made theme? (y/n): ").lower()
    if wants_themes in ['y', 'n']:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        
if wants_themes == 'y':
    for key in themes.keys(): print(" -", key)  # lists available themes
    theme_choice = None
    while theme_choice is None:
        theme_choice = get_valid_theme(themes)
    
    # applies pre-made themes
    font_color = themes[theme_choice]["font_color"]
    bg_color = themes[theme_choice]["bg_color"]
else:
    # customizes font color
    font_color = None
    while font_color is None:
        font_color = choose_color(
            "\nEnter your preferred font color as a word ('red') or as a hex ('#FF0000'), or press 'd' for default: ", "white")

    # customizes background color
    bg_color = None
    while bg_color is None:
        bg_color = choose_color(
            "\nEnter your preferred background color as a word ('blue') or as a hex ('#0000FF'), or press 'd' for default: ", "black")

# apply user preferences
label = tk.Label(root, font=(user_font, 70), fg=font_color, bg=bg_color)
label.pack(padx=10, pady=10)
root.deiconify()  # shows the window after set up is complete
print("Your personalized digital clock is now running!")

update_time()
root.mainloop()