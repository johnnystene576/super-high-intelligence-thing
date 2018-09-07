try: # Import libraries
    print("DEBUG: Importing libraries.")
    from tkinter import *
    import os, sys, time, json
except: # Catch errors
    print("ERROR: Failed to load libraries!")
    sys.exit(1)

try: # Load config file
    print("DEBUG: Loading configuration file")
    with open("config.json") as jsonfile:
        config = json.load(jsonfile)
    text_spacing = config["text_spacing"]
except: # Catch errors.
    print("ERROR: Couldn't load config.json!")
    sys.exit(2)

def drawWavyText(x, y, string):
    print("DEBUG: Drawing string \"" + string + "\" at position: X" + str(x) + "Y" + str(y))
    window.delete(all) # Clear screen
    background = window.create_rectangle(0, 0, config["window_width"], config["window_height"], fill = "#009FFF", outline = "#009FFF")
    direction = 0
    cy = y # Set current char y to given y
    cx = x # Do the same for x
    for char in string:
        window.create_text(cx, cy, text = char, fill="#FFFFFF", font=("Courier New", 24)) # Draw current char
        cx = cx + text_spacing
        if(direction == 0):
            cy = cy + text_spacing
            direction = 1
        else:
            cy = cy - text_spacing
            direction = 0
        
print("DEBUG: Creating window.")
root = Tk()
window = Canvas(root, width=config["window_width"], height=config["window_height"])
window.pack()
drawWavyText(16, 16, config["display_text"])
root.mainloop()
