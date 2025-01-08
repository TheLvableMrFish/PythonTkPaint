import tkinter as tk
from tkinter import ttk

# Global Var
is_holding = False

def on_click_press():
    global is_holding
    is_holding = True

def off_click_press():
    global is_holding
    is_holding = False
    

def get_pos(e):
    x = e.x
    y = e.y
    return x,y

def draw(e):
    x,y = get_pos(e)
    if(is_holding):
        canvas.create_oval((x, y, x, y), fill='black')
    

# setup
window = tk.Tk()
window.geometry('800x600')
window.title('Paint')

# canvas
canvas = tk.Canvas(window, bg='white', width=800, height=600)
canvas.pack()

# event
canvas.bind('<Motion>', lambda e: draw(e))

canvas.bind('<ButtonPress-1>', lambda event: on_click_press())
canvas.bind('<ButtonRelease-1>', lambda event: off_click_press())

# run
window.mainloop()