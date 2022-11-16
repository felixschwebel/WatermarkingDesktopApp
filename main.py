# Test-Image by Pawel Czerwinski on Unsplash

import tkinter
from tkinter import ttk
import sys
from PIL import Image, ImageDraw, ImageTk

# Apperance Configurations
FONT = ('SF Pro', 18, "bold")
BG = 'white'
FG = '#565656'
PAD = 30

# Window
window = tkinter.Tk()
window.title('Watermarking App')
window.config(bg=BG, padx=PAD)
window.minsize()

# Functions


# Labels
text1 = tkinter.Label(text='Your Watermark Text')
text1.config(bg=BG, fg=FG, font=FONT)
text1.grid(column=0, row=2, sticky=tkinter.W, pady=PAD)

text2 = tkinter.Label(text='Position')
text2.config(bg=BG, fg=FG, font=FONT)
text2.grid(column=0, row=3, sticky=tkinter.W, pady=PAD)


# Buttons
upload = tkinter.Button(text='Upload Image')
upload.config(font=FONT, fg=FG)
upload.grid(column=0, row=0, sticky=tkinter.W, pady=PAD)

download = tkinter.Button(text='Download Image')
download.config(font=FONT, fg=FG)
download.grid(column=2, row=0, sticky=tkinter.E, pady=PAD)

preview = tkinter.Button(text='Preview')
preview.config(font=FONT, fg=FG)
preview.grid(column=2, row=3, sticky=tkinter.E)


# Entry
personal_watermark = tkinter.Entry(width=40)
personal_watermark.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)

position = tkinter.ttk.Combobox(width=15)
position.grid(column=1, row=3, sticky=tkinter.W)


# Example Image
resize_factor = 2
width = int(1200/resize_factor)
height = int(700/resize_factor)
img = Image.open('test.png').resize((width, height))
photo_img = ImageTk.PhotoImage(img)
example_img = tkinter.Label(image=photo_img)
example_img.grid(column=0, row=1, columnspan=3)


window.mainloop()
