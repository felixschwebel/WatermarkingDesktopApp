# example.jpg by Jonny Gios from unsplash.com

import tkinter
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageTk

# Apperance Configurations
FONT = ('SF Pro', 18, "bold")
BG = 'white'
FG = '#565656'
PAD = 20
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 800
WATERMARK_EDGE_DISTANCE = 35

# Window
window = tkinter.Tk()
window.title('Watermarking App')
window.config(bg=BG, padx=PAD)
window.minsize()
window.resizable(False, False)


# ---------------------------- Functions ----------------------------
def upload_image():
    global text_container
    canvas.delete(text_container)
    global USER_IMG
    USER_IMG = prepare_img(get_file())
    canvas.itemconfig(img_container, image=USER_IMG)


def download_image():
    pass


def preview_picture():
    global text_container
    canvas.delete(text_container)

    # Get the position the user selected
    watermark_pos = position.get()
    # 'top left'
    if watermark_pos == 'top left':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2) + WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2) + WATERMARK_EDGE_DISTANCE
        anchor = tkinter.NW
    # 'top right'
    elif watermark_pos == 'top right':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2 + USER_IMG_WIDTH) - WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2) + WATERMARK_EDGE_DISTANCE
        anchor = tkinter.NE
    # 'bottom left'
    elif watermark_pos == 'bottom left':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2) + WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2 + USER_IMG_HEIGHT) - WATERMARK_EDGE_DISTANCE
        anchor = tkinter.SW
    # 'bottom right'
    elif watermark_pos == 'bottom right':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2 + USER_IMG_WIDTH) - WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2 + USER_IMG_HEIGHT) - WATERMARK_EDGE_DISTANCE
        anchor = tkinter.SE
    # 'center'
    else:
        width = int(CANVAS_WIDTH / 2)
        height = int(CANVAS_HEIGHT / 2)
        anchor = tkinter.CENTER

    # Get the size, color and type of the font
    if text_size.get() != '':
        size = int(text_size.get())
    else:
        size = 24

    if text_color.get() != '':
        color = text_color.get()
    else:
        color = "black"

    if text_font.get() != '':
        font = text_font.get()
    else:
        font = 'SF Pro'

    text_container = canvas.create_text(width, height, anchor=anchor,
                                        text=personal_watermark.get(),
                                        font=(font, size, 'normal'),
                                        fill=color)


def get_file():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title='Select your Image',
        filetypes=[('Image files', '*.jpg'), ('Image files', '*.png')]
    )
    return file_path


def prepare_img(file_path):
    global USER_IMG_WIDTH, USER_IMG_HEIGHT
    raw_img = Image.open(file_path)
    resize_factor = 1
    while raw_img.width > CANVAS_WIDTH or raw_img.height > CANVAS_HEIGHT:
        resize_factor -= 0.01
        USER_IMG_WIDTH = int(raw_img.width * resize_factor)
        USER_IMG_HEIGHT = int(raw_img.height * resize_factor)
        raw_img = raw_img.resize((USER_IMG_WIDTH, USER_IMG_HEIGHT))
    final_img = ImageTk.PhotoImage(raw_img)
    return final_img


# ---------------------- User Variables ----------------------
USER_IMG = None
USER_IMG_WIDTH = CANVAS_WIDTH
USER_IMG_HEIGHT = CANVAS_HEIGHT
USER_TEXT = None
USER_TEXT_X = None
USER_TEXT_Y = None

# ---------------------------- UI ----------------------------
# Example Image
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                        background=BG, borderwidth=0, highlightthickness=0)
photo_img = tkinter.PhotoImage(file='start.png')

# User Image
img_container = canvas.create_image(int(CANVAS_WIDTH / 2), int(CANVAS_HEIGHT / 2),
                                    image=photo_img, anchor=tkinter.CENTER)
text_container = canvas.create_text(int(CANVAS_WIDTH / 2), int(CANVAS_HEIGHT / 2), text='')
canvas.grid(column=0, row=1, columnspan=4)

# Labels
text_mark = tkinter.Label(text='Your Watermark Text')
text_mark.config(bg=BG, fg=FG, font=FONT)
text_mark.grid(column=0, row=2, sticky=tkinter.W, pady=PAD)

text_position = tkinter.Label(text='Position')
text_position.config(bg=BG, fg=FG, font=FONT)
text_position.grid(column=0, row=3, sticky=tkinter.W, pady=PAD)

text_font = tkinter.Label(text='Text Font')
text_font.config(bg=BG, fg=FG, font=FONT)
text_font.grid(column=2, row=3, sticky=tkinter.W, pady=PAD)

text_color = tkinter.Label(text='Text Color')
text_color.config(bg=BG, fg=FG, font=FONT)
text_color.grid(column=0, row=4, sticky=tkinter.W, pady=PAD)

text_size = tkinter.Label(text='Text Size')
text_size.config(bg=BG, fg=FG, font=FONT)
text_size.grid(column=2, row=4, sticky=tkinter.W, pady=PAD)

# Entry
personal_watermark = tkinter.Entry(width=42)
personal_watermark.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)

position = tkinter.ttk.Combobox(width=15, state='readonly')
position['values'] = (
    'top left',
    'top right',
    'bottom left',
    'bottom right',
    'center',
)
position.grid(column=1, row=3, sticky=tkinter.W)

text_font = tkinter.ttk.Combobox(width=15, state='readonly')
text_font['values'] = (
    'Arial',
    'Courier',
    'SF Pro',
    'Times New Roman',
)
text_font.grid(column=3, row=3, sticky=tkinter.W)

text_color = tkinter.ttk.Combobox(width=15, state='readonly')
text_color['values'] = (
    'black',
    'white',
    'gray',
    'gray20',
    'gray30',
    'gray40',
    'gray50',
    'gray60',
    'gray70',
    'gray80',
    'gray90',
)
text_color.grid(column=1, row=4, sticky=tkinter.W)

text_size = tkinter.ttk.Combobox(width=15, state='readonly')
text_size['values'] = (14, 16, 18, 20, 22, 24, 28, 30, 36, 40, 50, 60)
text_size.grid(column=3, row=4, sticky=tkinter.W)

# Buttons
upload = tkinter.Button(text='Upload Image', command=upload_image)
upload.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
upload.grid(column=0, row=0, sticky=tkinter.W, pady=PAD)

download = tkinter.Button(text='Download Image', command=download_image)
download.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
download.grid(column=3, row=0, sticky=tkinter.E, pady=PAD)

preview = tkinter.Button(text='Preview', command=preview_picture)
preview.config(font=FONT, fg=FG, bd=0, relief='flat', pady=5)
preview.grid(column=3, row=2, sticky=tkinter.E)

window.mainloop()
