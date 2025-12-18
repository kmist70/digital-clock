import tkinter as tk

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
def choose_color(root, prompt, default):
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