import tkinter as tk
from tkinter import ttk

# Global Var
is_holding_left_click = False
brush_size = 2
is_alt_holding = False

def on_click_press():
    global is_holding_left_click
    is_holding_left_click = True

def off_click_press():
    global is_holding_left_click
    is_holding_left_click = False 

def get_pos(e):
    x = e.x
    y = e.y
    return x,y

def draw(e):
    x,y = get_pos(e)
    if(is_holding_left_click):
        canvas.create_oval((
            x - (brush_size / 2), 
            y - (brush_size / 2), 
            x + (brush_size / 2), 
            y + (brush_size / 2)
            ), fill='black')
        
def on_alt_press():
    global is_alt_holding
    is_alt_holding = True

def on_alt_release():
    global is_alt_holding
    is_alt_holding = False

def brush_size_adjust(e):
    global brush_size
    global is_alt_holding
    
    if is_alt_holding:

        if e.delta > 0:
            brush_size += 1
        else:
            brush_size -= 1
            if brush_size < 1:
                brush_size = 1

# setup
window = tk.Tk()
window.geometry('800x600')
window.title('Paint')

# canvas
canvas = tk.Canvas(window, bg='white', width=800, height=600)
canvas.pack()

# event
canvas.bind('<Motion>', lambda e: draw(e))

# Only draw when pressed
canvas.bind('<ButtonPress-1>', lambda event: on_click_press())
canvas.bind('<ButtonRelease-1>', lambda event: off_click_press())

# Change brush size
canvas.bind('<MouseWheel>', brush_size_adjust)
window.bind('<Alt_L>', lambda e: on_alt_press())
window.bind('<KeyRelease-Alt_L>', lambda e: on_alt_release())

# run
window.mainloop()