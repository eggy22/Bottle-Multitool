import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image
import io

def generate_qr_code():
    link = link_entry.get()

    if link:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', back_color='white')

        # Convert QR code image to Tkinter-compatible format
        img_io = io.BytesIO()
        qr_image.save(img_io, 'PNG')
        img_io.seek(0)
        img = Image.open(img_io)
        img = img.resize((300, 300), Image.ANTIALIAS)
        qr_img = ImageTk.PhotoImage(img)

        qr_label.config(image=qr_img)
        qr_label.image = qr_img
        link_label.config(text="Link: " + link)
    else:
        messagebox.showwarning("Error", "Please enter a link.")

# Create the Tkinter window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x500")
window.configure(background="#F7F7F7")

# Create the "Paste your link" title label
title_label = tk.Label(window, text="Paste your link", font=("Arial", 16, "bold"), bg="#F7F7F7")
title_label.pack(pady=10)

# Create the QR code image label
qr_label = tk.Label(window, bg="#F7F7F7")
qr_label.pack()

# Create the link label
link_label = tk.Label(window, font=("Arial", 12), wraplength=300, bg="#F7F7F7")
link_label.pack()

# Create the link entry field
link_entry = tk.Entry(window, width=40, font=("Arial", 12))
link_entry.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate", command=generate_qr_code, font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.FLAT)
generate_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
