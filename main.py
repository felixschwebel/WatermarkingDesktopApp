# example.jpg by Jonny Gios from unsplash.com

import tkinter
from tkinter import ttk, filedialog
from PIL import Image, ImageDraw, ImageTk, ImageFont

# Apperance Configurations
FONT = ('SF Pro', 18, "bold")
BG = 'white'
FG = '#565656'
PAD = 20
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 800
WATERMARK_EDGE_DISTANCE = 25

# Window
window = tkinter.Tk()
window.title('Watermarking App')
window.config(bg=BG, padx=PAD)
window.minsize()
window.resizable(False, False)


# ---------------------------- Functions ----------------------------
def upload_image():
    global text_container, USER_IMG_RESIZED, RAW_IMG
    canvas.delete(text_container)
    USER_IMG_RESIZED = prepare_img(get_file())
    RAW_IMG = Image.open(USER_IMG_FILE)
    canvas.itemconfig(img_container, image=USER_IMG_RESIZED)


def download_image():
    preview_picture()
    with Image.open(USER_IMG_FILE).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        size_compensation = int(USER_SIZE/RESIZE_FACTOR)
        fnt = ImageFont.truetype(USER_FONT, size_compensation)
        # drawing context
        d = ImageDraw.Draw(txt)
        d.text((USER_IMG_X, USER_IMG_Y), anchor=USER_IMG_ANCHOR,
               text=USER_TEXT, font=fnt, fill=USER_COLOR)
        new_image = Image.alpha_composite(base, txt)
        new_image.show()


def preview_picture():
    global text_container, USER_TEXT, USER_IMG_X, USER_IMG_Y, USER_IMG_ANCHOR
    # Delete any previous watermarks
    canvas.delete(text_container)

    USER_TEXT = personal_watermark.get()

    # Get the position the user selected
    watermark_pos = position.get()

    # 'top left'
    if watermark_pos == 'top left':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2) + WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2) + WATERMARK_EDGE_DISTANCE
        anchor = tkinter.NW

        USER_IMG_X = int(WATERMARK_EDGE_DISTANCE / RESIZE_FACTOR)
        USER_IMG_Y = int(WATERMARK_EDGE_DISTANCE / RESIZE_FACTOR)
        USER_IMG_ANCHOR = 'lt'

    # 'top right'
    elif watermark_pos == 'top right':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2 + USER_IMG_WIDTH) - WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2) + WATERMARK_EDGE_DISTANCE
        anchor = tkinter.NE

        USER_IMG_X = int(RAW_IMG.size[0]-WATERMARK_EDGE_DISTANCE / RESIZE_FACTOR)
        USER_IMG_Y = int(WATERMARK_EDGE_DISTANCE / RESIZE_FACTOR)
        USER_IMG_ANCHOR = 'rt'

    # 'bottom left'
    elif watermark_pos == 'bottom left':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2) + WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2 + USER_IMG_HEIGHT) - WATERMARK_EDGE_DISTANCE
        anchor = tkinter.SW

        USER_IMG_X = int(WATERMARK_EDGE_DISTANCE/RESIZE_FACTOR)
        USER_IMG_Y = int(RAW_IMG.size[1]-WATERMARK_EDGE_DISTANCE/RESIZE_FACTOR)
        USER_IMG_ANCHOR = 'ls'

    # 'bottom right'
    elif watermark_pos == 'bottom right':
        width = int((CANVAS_WIDTH - USER_IMG_WIDTH) / 2 + USER_IMG_WIDTH) - WATERMARK_EDGE_DISTANCE
        height = int((CANVAS_HEIGHT - USER_IMG_HEIGHT) / 2 + USER_IMG_HEIGHT) - WATERMARK_EDGE_DISTANCE
        anchor = tkinter.SE

        USER_IMG_X = int(RAW_IMG.size[0] - WATERMARK_EDGE_DISTANCE / RESIZE_FACTOR)
        USER_IMG_Y = int(RAW_IMG.size[1]-WATERMARK_EDGE_DISTANCE/RESIZE_FACTOR)
        USER_IMG_ANCHOR = 'rs'

    # 'center'
    else:
        width = int(CANVAS_WIDTH / 2)
        height = int(CANVAS_HEIGHT / 2)
        anchor = tkinter.CENTER

        USER_IMG_X = int(RAW_IMG.size[0]/2)
        USER_IMG_Y = int(RAW_IMG.size[1]/2)
        USER_IMG_ANCHOR = 'mm'

    # Get the size, color and type of the font
    global USER_SIZE, USER_COLOR, USER_FONT

    if text_size.get() != '':
        USER_SIZE = int(text_size.get())

    if text_color.get() != '':
        USER_COLOR = text_color.get()

    if text_font.get() != '':
        USER_FONT = text_font.get()

    text_container = canvas.create_text(width, height, anchor=anchor,
                                        text=USER_TEXT,
                                        font=(USER_FONT, USER_SIZE, 'normal'),
                                        fill=USER_COLOR)


def get_file():
    global USER_IMG_FILE
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title='Select your Image',
        filetypes=[('Image files', '*.jpg'), ('Image files', '*.png')]
    )
    USER_IMG_FILE = file_path
    return file_path


def prepare_img(file_path):
    global USER_IMG_WIDTH, USER_IMG_HEIGHT, RESIZE_FACTOR
    factor = 1
    resize_img = Image.open(file_path)
    while resize_img.width > CANVAS_WIDTH or resize_img.height > CANVAS_HEIGHT:
        factor -= 0.01
        USER_IMG_WIDTH = int(resize_img.width * factor)
        USER_IMG_HEIGHT = int(resize_img.height * factor)
        RESIZE_FACTOR *= factor
        resize_img = resize_img.resize((USER_IMG_WIDTH, USER_IMG_HEIGHT))
    final_img = ImageTk.PhotoImage(resize_img)
    return final_img


# ---------------------- User Variables ----------------------
USER_IMG_FILE = 'start.png'
RAW_IMG = Image.open(USER_IMG_FILE)
USER_IMG_RESIZED = None
RESIZE_FACTOR = 1
USER_IMG_WIDTH = CANVAS_WIDTH
USER_IMG_HEIGHT = CANVAS_HEIGHT
USER_TEXT = ''
USER_COLOR = 'black'
USER_SIZE = 24
USER_FONT = 'Arial'
USER_IMG_X = 0
USER_IMG_Y = 0
USER_IMG_ANCHOR = ''

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
    'Times New Roman',
)
text_font.grid(column=3, row=3, sticky=tkinter.W)

text_color = tkinter.ttk.Combobox(width=15, state='readonly')
text_color['values'] = (
    'black',
    'white',
    'gray',
    'red',
    'yellow',
    'green',
    'blue'
)
text_color.grid(column=1, row=4, sticky=tkinter.W)

text_size = tkinter.ttk.Combobox(width=15, state='readonly')
text_size['values'] = (6, 8, 10, 14, 16, 18, 20, 22, 24, 28, 30, 36, 40, 50, 60)
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
