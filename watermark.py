from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog

class Watermark():
    def __init__(self):
        pass
    def single_mark(self,input_image_path, watermark_text, texture, color, size, position):
        original_image = Image.open(input_image_path).convert("RGBA")
        original_width, original_height = original_image.size
        txt = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", size)
        draw = ImageDraw.Draw(txt)

        textbbox = draw.textbbox((0, 0), watermark_text, font=font)
        textwidth = textbbox[2] - textbbox[0]
        textheight = textbbox[3] - textbbox[1]

        width, height = original_image.size

        if position == "Top":
            x, y = (width - textwidth) // 2, 10
        elif position == "Bottom":
            x, y = (width - textwidth) // 2, height - textheight - 10
        elif position == "Left":
            x, y = 10, (height - textheight) // 2
        elif position == "Right":
            x, y = width - textwidth - 10, (height - textheight) // 2
        elif position == "Top-left":
            x, y = 10, 10
        elif position == "Top-right":
            x, y = width - textwidth - 10, 10
        elif position == "Bottom-left":
            x, y = 10, height - textheight - 10
        elif position == "Bottom-right":
            x, y = width - textwidth - 10, height - textheight - 10
        elif position == "Center":
            x, y = (width - textwidth) // 2, (height - textheight) // 2
        else:
            x, y = 10, 10

        draw.text((x, y), watermark_text, font=font, fill=color + (texture,))

        watermarked = Image.alpha_composite(original_image, txt)
        watermarked = watermarked.convert("RGB")

        output_path = filedialog.asksaveasfilename(
            title="Save Watermarked Image",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
        )

        if output_path:
            watermarked.save(output_path, "JPEG")

    def multiple_watermark(self,input_image_path, watermark_text, direction, texture, color, size, distance):
        original_image = Image.open(input_image_path).convert("RGBA")
        original_width, original_height = original_image.size
        original_image = original_image.rotate(direction, expand=True)
        txt = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

        font = ImageFont.truetype("arial.ttf", size)
        draw = ImageDraw.Draw(txt)

        textbbox = draw.textbbox((0, 0), watermark_text, font=font)
        textwidth = textbbox[2] - textbbox[0]
        textheight = textbbox[3] - textbbox[1]

        width, height = original_image.size

        for i in range(10, width, distance + textwidth):
            for j in range(10, height, distance + textheight):
                draw.text((i, j), watermark_text, font=font, fill=color + (texture,))

        watermarked = Image.alpha_composite(original_image, txt)
        watermarked = watermarked.rotate(direction * -1, expand=True)

        left = (watermarked.width - original_width) / 2
        upper = (watermarked.height - original_height) / 2
        right = left + original_width
        lower = upper + original_height
        box = (left, upper, right, lower)

        watermarked = watermarked.crop(box)
        watermarked = watermarked.convert("RGB")

        output_path = filedialog.asksaveasfilename(
            title="Save Watermarked Image",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
        )

        if output_path:
            watermarked.save(output_path, "JPEG")
