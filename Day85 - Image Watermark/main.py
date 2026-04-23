import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

# ====== GLOBAL STATE ======
original_img = None
working_img = None

# ====== FUNCTIONS ======

def upload_image():
    global original_img, working_img

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )

    if not file_path:
        return

    original_img = Image.open(file_path).convert("RGBA")
    working_img = original_img.copy()

    display_image(working_img)


def display_image(img):
    preview = img.copy()
    preview.thumbnail((400, 400))

    tk_img = ImageTk.PhotoImage(preview)
    panel.config(image=tk_img)
    panel.image = tk_img


def add_text_watermark():
    global working_img

    if working_img is None:
        messagebox.showerror("Error", "Upload an image first.")
        return

    text = text_entry.get().strip()
    if not text:
        messagebox.showerror("Error", "Enter watermark text.")
        return

    img = working_img.copy()
    drawable = ImageDraw.Draw(img)

    width, height = img.size

    try:
        font = ImageFont.truetype("arial.ttf", int(size_scale.get()))
    except:
        font = ImageFont.load_default()

    bbox = drawable.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = width - text_width - 10
    y = height - text_height - 10

    opacity = int(opacity_scale.get())

    # Create transparent layer for text
    text_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_layer)

    text_draw.text((x, y), text, font=font, fill=(255, 255, 255, opacity))

    working_img = Image.alpha_composite(img, text_layer)

    display_image(working_img)


def add_logo_watermark():
    global working_img

    if working_img is None:
        messagebox.showerror("Error", "Upload an image first.")
        return

    logo_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if not logo_path:
        return

    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo
    logo_size = int(logo_scale.get())
    logo.thumbnail((logo_size, logo_size))

    img = working_img.copy()

    x = img.width - logo.width - 10
    y = img.height - logo.height - 10

    img.paste(logo, (x, y), logo)

    working_img = img

    display_image(working_img)


def reset_image():
    global working_img

    if original_img:
        working_img = original_img.copy()
        display_image(working_img)


def save_image():
    if working_img is None:
        messagebox.showerror("Error", "Nothing to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")]
    )

    if not file_path:
        return

    # Convert to RGB if saving as JPG
    if file_path.endswith(".jpg"):
        working_img.convert("RGB").save(file_path)
    else:
        working_img.save(file_path)

    messagebox.showinfo("Saved", "Image saved successfully!")


# ====== UI ======
root = tk.Tk()
root.title("Watermark App")
root.geometry("500x700")

panel = tk.Label(root)
panel.pack(pady=10)

tk.Button(root, text="Upload Image", command=upload_image).pack(pady=5)

# ---- TEXT WATERMARK ----
tk.Label(root, text="Watermark Text:").pack()
text_entry = tk.Entry(root, width=30)
text_entry.pack()

tk.Label(root, text="Font Size").pack()
size_scale = tk.Scale(root, from_=10, to=100, orient="horizontal")
size_scale.set(30)
size_scale.pack()

tk.Label(root, text="Opacity").pack()
opacity_scale = tk.Scale(root, from_=50, to=255, orient="horizontal")
opacity_scale.set(150)
opacity_scale.pack()

tk.Button(root, text="Add Text Watermark", command=add_text_watermark).pack(pady=5)

# ---- LOGO WATERMARK ----
tk.Label(root, text="Logo Size").pack()
logo_scale = tk.Scale(root, from_=50, to=300, orient="horizontal")
logo_scale.set(100)
logo_scale.pack()

tk.Button(root, text="Add Logo Watermark", command=add_logo_watermark).pack(pady=5)

# ---- CONTROL BUTTONS ----
tk.Button(root, text="Reset Image", command=reset_image).pack(pady=5)
tk.Button(root, text="Save Image", command=save_image).pack(pady=5)

root.mainloop()