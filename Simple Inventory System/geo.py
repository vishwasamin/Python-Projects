import tkinter as tk
import tkinter.messagebox as tkMessageBox

root = tk.Tk()
root.title('Tkinter Window - Center')

window_width = 1000
window_height = 550

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
result = tkMessageBox.askquestion('Simple Inventory System', 'Do you want to exit?', icon="warning")
if result == 'yes':
        root.destroy()
        exit()

root.mainloop()