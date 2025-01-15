import tkinter as tk
from tkinter import ttk

# Global Var
is_holding_left_click = False
is_holding_right_click = False
is_alt_holding = False

# Global Styling
brush_size = 2
brush_color = 'black'


def on_left_click_press():
    global is_holding_left_click
    is_holding_left_click = True

def off_left_click_press():
    global is_holding_left_click
    is_holding_left_click = False

def on_right_click_press():
    global is_holding_right_click
    is_holding_right_click = True

def off_right_click_press():
    global is_holding_right_click
    is_holding_right_click = False 

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
            ), fill=brush_color,
            outline='')
    if(is_holding_right_click):
        canvas.create_oval((
            x - (brush_size / 2), 
            y - (brush_size / 2), 
            x + (brush_size / 2), 
            y + (brush_size / 2)
            ), fill='white',
            outline= '')
        
def on_alt_press():
    global is_alt_holding
    is_alt_holding = True

def on_alt_release():
    global is_alt_holding
    is_alt_holding = False

def brush_size_adjust(e):
    global brush_size
    global is_alt_holding
    global brush_size_scroller
    
    if is_alt_holding:

        if e.delta > 0 and brush_size < 25:
            brush_size += 1
        elif e.delta < 0 and brush_size > 0:
            brush_size -= 1
        print(brush_size)
    
    brush_size = max(0, min(brush_size, 50))
    brush_size_scroller.set(int(float(brush_size)))

def brush_size_scroller_adjust(size):
    global brush_size
    brush_size = size
    brush_size_scroller.set(int(float(brush_size)))

def on_color_change(color):
    global brush_color
    brush_color = color

# setup
window = tk.Tk()
window.geometry('800x600')
window.title('Paint')
window.iconbitmap('./media/paint.ico')

color_frame = tk.Frame(window)
canvas_frame = tk.Frame(window)
brush_frame = tk.Frame(window)
brush_label_frame = tk.Frame(brush_frame)
brush_slider_frame = tk.Frame(brush_frame)

# color canvas
canvas_paint_options = tk.Canvas(color_frame, bg='lightGray', bd=1, relief='solid', width=800, height=40)
canvas_paint_options.pack()

# canvas
canvas = tk.Canvas(canvas_frame, bg='white', bd=0, relief='flat', width=800, height=505)
canvas.pack()

# Define colors and button info
button_colors = ['black', 'red', 'orange', 'brown', 'green', 'yellow', 'blue', 'gray']
text_color = ['white', 'white', 'white', 'white', 'white', 'black', 'white', 'white']
num_buttons = len(button_colors)
button_width = 800 / (num_buttons * 2)
spacing = (800 - num_buttons * button_width + button_width) / (num_buttons + 1)

# Create color buttons
for i in range(num_buttons):
    x_position = (i + 1) * spacing + i * button_width

    button = tk.Button(window, text=f'{button_colors[i]}', width=8, height=1, bg=button_colors[i], fg=text_color[i], command=lambda i=i: on_color_change(button_colors[i]))
    canvas_paint_options.create_window(x_position, 22, window=button)

# event
canvas.bind('<Motion>', lambda e: draw(e))

# Only draw when pressed
canvas.bind('<ButtonPress-1>', lambda event: on_left_click_press())
canvas.bind('<ButtonRelease-1>', lambda event: off_left_click_press())

canvas.bind('<ButtonPress-3>', lambda event: on_right_click_press())
canvas.bind('<ButtonRelease-3>', lambda event: off_right_click_press())

# Change brush size
canvas.bind('<MouseWheel>', brush_size_adjust)
window.bind('<Alt_L>', lambda e: on_alt_press())
window.bind('<KeyRelease-Alt_L>', lambda e: on_alt_release())

# Slider label



brush_size_scroller = tk.IntVar(value=2)

brush_label_size = ttk.Label(brush_label_frame, textvariable=brush_size_scroller)
brush_label_size.pack(side='right')

brush_label = ttk.Label(brush_label_frame, text='Brush Size')
brush_label.pack(side='right')


# Slider


brush_scale = ttk.Scale(
    brush_slider_frame, 
    command= lambda value: brush_size_scroller_adjust(brush_size_scroller.get()), 
    from_=1, to=25,
    length= 545,
    orient= 'horizontal',
    variable=brush_size_scroller
)
brush_scale.pack(side='left')



color_frame.pack(side='top')
brush_frame.pack(side='top')
canvas_frame.pack(side='top', expand=True, fill='both')

brush_label_frame.pack()
brush_slider_frame.pack()

# run
window.mainloop()