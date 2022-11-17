import tkinter
from tkinter import ttk
import sys
from PIL import Image, ImageDraw, ImageTk

# Apperance Configurations
FONT = ('SF Pro', 18, "bold")
BG = 'white'
FG = '#565656'
PAD = 30
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 800

# Window
window = tkinter.Tk()
window.title('Watermarking App')
window.config(bg=BG, padx=PAD)
window.minsize()
#window.resizable(False, False)


# Functions
def load_picture():
    canvas.itemconfig(img_container, image=user_image)

def save_picture():
    pass


def preview_picture():
    pass


def get_user_img():
    raw_img = Image.open('example.jpg')
    resize_factor = 1
    while raw_img.width > CANVAS_WIDTH or raw_img.height > CANVAS_HEIGHT:
        resize_factor -= 0.01
        raw_img = raw_img.resize((int(raw_img.width*resize_factor), int(raw_img.height*resize_factor)))
    final_img = ImageTk.PhotoImage(raw_img)
    return final_img


# Example Image
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=BG, borderwidth=0, highlightthickness=0)
photo_img = tkinter.PhotoImage(file='start.png')

# User Image
user_image = get_user_img()

img_container = canvas.create_image(int(CANVAS_WIDTH/2), int(CANVAS_HEIGHT/2), image=photo_img, anchor=tkinter.CENTER)
canvas.grid(column=0, row=1, columnspan=3)


# Labels
text1 = tkinter.Label(text='Your Watermark Text')
text1.config(bg=BG, fg=FG, font=FONT)
text1.grid(column=0, row=2, sticky=tkinter.W, pady=PAD)

text2 = tkinter.Label(text='Position')
text2.config(bg=BG, fg=FG, font=FONT)
text2.grid(column=0, row=3, sticky=tkinter.W, pady=PAD)


# Buttons
upload = tkinter.Button(text='Upload Image', command=load_picture)
upload.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
upload.grid(column=0, row=0, sticky=tkinter.W, pady=PAD)

download = tkinter.Button(text='Download Image', command=save_picture)
download.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
download.grid(column=2, row=0, sticky=tkinter.E, pady=PAD)

preview = tkinter.Button(text='Preview', command=preview_picture)
preview.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
preview.grid(column=2, row=3, sticky=tkinter.E)


# Entry
personal_watermark = tkinter.Entry(width=42)
personal_watermark.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)
personal_watermark.focus()

position = tkinter.ttk.Combobox(width=15, state='readonly')
position['values'] = (
    'top left',
    'top right',
    'bottom left',
    'bottom right',
    'center',
)
position.grid(column=1, row=3, sticky=tkinter.W)



window.mainloop()
