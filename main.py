from tkinter import *
from tkinter import filedialog,colorchooser,messagebox
from PIL import Image,ImageTk
from watermark import Watermark

watermark=Watermark()

color=(255,255,255)
def choose_color():
    global  color
    color_code = colorchooser.askcolor(title="Choose color")
    color= color_code[0]

def disappear_button(button):
    button.place_forget()
    button.config(state=DISABLED)

def reupload_image():
    canvas.delete("all")
    canvas.create_image(392, 290, image=bg_image, anchor=CENTER)

    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    button.config(state=NORMAL)

    disappear_button(multiple)
    disappear_button(single)
    disappear_button(reupload_button)

def process_single_watermark():
    watermark_text = Watermark.get()
    if watermark_text==""or watermark==" ":
        messagebox.showerror("Missing", "For Watermark text is required")
        return
    texture = Texture.get()
    size = Size_button.get()
    position=single_direction.get()
    watermark.single_mark(file, watermark_text, int(texture), color, int(size), position)

def process_multiple_watermark():
    watermark_text=Watermark.get()
    if watermark_text==""or watermark==" ":
        messagebox.showerror("Missing", "For Watermark text is required")
        return
    texture=Texture.get()
    if selected_direction.get()=="Horizontal":
        direction=0
    if selected_direction.get()=="Vertical":
        direction=90
    if selected_direction.get()=="Diagonal":
        direction=45
    if selected_direction.get()=="Diagonal2":
        direction=315
    size=Size_button.get()
    distance=distance_button.get()
    watermark.multiple_watermark(file, watermark_text, int(direction), int(texture),color,int(size),int(distance))

def  single_watermark():
    undo_button.place(relx=0.05, rely=0.05)
    undo_button.config(state=NORMAL)

    label.place(relx=0.01, rely=0.95)
    label.config(state=NORMAL)

    Watermark.place(relx=0.3, rely=0.96)
    Watermark.config(state=NORMAL)

    Add_single_button.place(relx=0.8, rely=0.94)
    Add_single_button.config(state=NORMAL)

    Texture_label.place(relx=0.01, rely=0.87)
    Texture_label.config(state=NORMAL)

    Texture.place(relx=0.37, rely=0.87)
    Texture.config(state=NORMAL)

    Direction_label.place(relx=0.45, rely=0.87)
    Direction_label.config(state=NORMAL)

    single_direction_button.place(relx=0.8, rely=0.87)
    single_direction_button.config(state=NORMAL)

    color_button.place(relx=0.05, rely=0.8)
    color_button.config(state=NORMAL)

    Text_size_label.place(relx=0.24, rely=0.81)
    Text_size_label.config(state=NORMAL)

    Size_button.place(relx=0.37, rely=0.81)
    Size_button.config(state=NORMAL)

    disappear_button(multiple)
    disappear_button(single)
    disappear_button(reupload_button)
def undo():
    disappear_button(undo_button)
    disappear_button(label)
    disappear_button(Add_button)
    disappear_button(Watermark)
    disappear_button(Texture)
    disappear_button(Texture_label)
    disappear_button(Direction_label)
    disappear_button(Direction)
    disappear_button(Text_size_label)
    disappear_button(Size_button)
    disappear_button(Text_distance_label)
    disappear_button(distance_button)
    disappear_button(single_direction_button)
    disappear_button(color_button)
    disappear_button(Add_single_button)

    reupload_button.place(relx=0.05, rely=0.05)
    reupload_button.config(state=NORMAL)

    multiple.place(relx=0.7, rely=0.9)
    multiple.config(state=NORMAL)

    single.place(relx=0.1, rely=0.9)
    single.config(state=NORMAL)

def multiple_watermark():
    undo_button.place(relx=0.05, rely=0.05)
    undo_button.config(state=NORMAL)

    label.place(relx=0.01,rely=0.95)
    label.config(state=NORMAL)

    Watermark.place(relx=0.3,rely=0.96)
    Watermark.config(state=NORMAL)

    disappear_button(multiple)
    disappear_button(single)
    disappear_button(reupload_button)

    Add_button.place(relx=0.8,rely=0.94)
    Add_button.config(state=NORMAL)

    Texture_label.place(relx=0.01,rely=0.87)
    Texture_label.config(state=NORMAL)

    Texture.place(relx=0.37,rely=0.87)
    Texture.config(state=NORMAL)

    Direction_label.place(relx=0.45,rely=0.87)
    Direction_label.config(state=NORMAL)

    Direction.place(relx=0.8,rely=0.87)
    Direction.config(state=NORMAL)

    color_button.place(relx=0.05,rely=0.8)
    color_button.config(state=NORMAL)

    Text_size_label.place(relx=0.24,rely=0.81)
    Text_size_label.config(state=NORMAL)

    Size_button.place(relx=0.37,rely=0.81)
    Size_button.config(state=NORMAL)

    Text_distance_label.place(relx=0.63,rely=0.81)
    Text_distance_label.config(state=NORMAL)

    distance_button.place(relx=0.82,rely=0.81)
    distance_button.config(state=NORMAL)


def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
    )
    try:
        if file_path:
            img = Image.open(file_path)

            img_ratio = img.width / img.height
            canvas_ratio = 780 / 580

            if img_ratio > canvas_ratio:
                new_width = 780
                new_height = int(680 / img_ratio)
            else:
                new_height = 580
                new_width = int(580 * img_ratio)

            img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img_resized)

            canvas.delete("all")
            canvas.create_image(398, 290, image=img_tk, anchor=CENTER)
            canvas.image = img_tk
            disappear_button(button)

            global file
            file = file_path
            global reupload_button

            reupload_button.config(state=NORMAL)
            multiple.config(state=NORMAL)
            single.config(state=NORMAL)

            reupload_button.place(relx=0.05, rely=0.05)
            multiple.place(relx=0.7, rely=0.9)
            single.place(relx=0.1, rely=0.9)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        return

window = Tk()
window.title("Watermark")
window.config(padx=10, pady=10)
window.maxsize(810, 600)
window.minsize(810, 600)
canvas = Canvas(window, width=780, height=580)
canvas.grid(column=1, row=1)
image = Image.open("assets/colorful-painting-camera-watercolor-white-background_608451-992.jpg")
img_resized = image.resize((780, 580), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(img_resized)
canvas.create_image(392, 290, image=bg_image, anchor=CENTER)

button = Button(window, text="Upload your image", command=upload_image,pady=3,padx=5,font=("Arial",13,"bold"),relief="raised",borderwidth=3,bg="#8DECB4",fg="#141E46")
button.place(relx=0.5, rely=0.5, anchor=CENTER)

label=Label(window,pady=3,padx=5,font=("Arial",13,"bold"),text="Enter Text for watermark")

Add_button = Button(window, text="Add Watermark", bg="#E6FF94", fg="#141E46", pady=3, padx=4,
                    font=("Arial", 13, "bold"),command=process_multiple_watermark)

reupload_button = Button(window, text="Reupload", bg="#FF6969", fg="#141E46", pady=3, padx=4, font=("Arial", 13, "bold"),
                     command=reupload_image)

multiple= Button(window, text="Multiple Watermark", bg="#E6FF94", fg="#141E46", pady=3, padx=4,
                    font=("Arial", 13, "bold"),command=multiple_watermark)

single= Button(window, text="Single Watermark", bg="#E6FF94", fg="#141E46", pady=3, padx=4,
                    font=("Arial", 13, "bold"),command=single_watermark)

undo_button = Button(window, text="Undo", bg="#FF6969", fg="#141E46", pady=3, padx=4, font=("Arial", 13, "bold"),
                     command=undo)

Texture_label=Label(window,pady=3,padx=5,font=("Arial",13,"bold"),text="Select value of watermark texture")
Texture = Spinbox(window, from_=1, to=255, width=5,font=("Arial", 13, "bold"))
Direction_label=Label(window,pady=3,padx=5,font=("Arial",13,"bold"),text="Select the direction of watermark")

Direction_list = ["Horizontal", "Vertical", "Diagonal", "Diagonal2"]

selected_direction = StringVar()
selected_direction.set(Direction_list[0])

Direction = OptionMenu(window, selected_direction,*Direction_list)

Direction.config(font=("Arial", 13, "bold"))

color_button = Button(window, text = "Select color",font=("Arial", 13, "bold"),command = choose_color)

Text_size_label= Label(window,pady=3,padx=5,font=("Arial",13,"bold"),text="Text Size")

Size_button=Spinbox(window, from_=1, to=150, width=5,font=("Arial", 13, "bold"))

Text_distance_label=Label(window,pady=3,padx=5,font=("Arial",13,"bold"),text="Text distance")

distance_button=Spinbox(window, from_=1, to=350, width=5,font=("Arial", 13, "bold"))

Add_single_button = Button(window, text="Add Watermark", bg="#E6FF94", fg="#141E46", pady=3, padx=4,
                    font=("Arial", 13, "bold"),command=process_single_watermark)

Single_Direction_list = ["Top", "Bottom", "Left", "Right","Top-left","Top-right","Bottom-left","Bottom-right","Center"]
single_direction = StringVar()
single_direction.set(Single_Direction_list[0])
single_direction_button = OptionMenu(window, single_direction,*Single_Direction_list)

Watermark=Entry(width=60)
window.mainloop()
