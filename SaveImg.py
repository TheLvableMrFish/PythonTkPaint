import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

def save_img(canvas):
    # Open save as dialog and select file location and name
    file_name = filedialog.asksaveasfilename(
        # Default file type
        defaultextension='.png',
        # File type options
        filetypes=[('PNG Files', '*.png'), ('All Files', '*.*')],
        title='Save As'
    )

    if file_name:
        # Get canvas size
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        # Create an image with the same size as the canvas
        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)

        # Get the brush strokes and edits to canvas
        items = canvas.find_all()

        for item in items:
            item_type = canvas.type(item)

            if item_type == 'oval':
                coords = canvas.coords(item)
                fill_color = canvas.itemcget(item, 'fill')

                # Draw the same oval on Pillow image
                draw.ellipse(
                    [coords[0], coords[1], coords[2], coords[3]],
                    fill=fill_color,
                    outline=fill_color
                )
        # Save Image
        image.save(file_name)