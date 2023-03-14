import qrcode
import tkinter as tk
from tkinter import filedialog

def create_qr():
    # Get the text to encode from the user
    text = entry.get()

    # Create a QR code object
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    # Get the filename to save the QR code image as
    filename = filedialog.asksaveasfilename(defaultextension=".png")

    # Save the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    # Close the Tkinter window
    window.destroy()

# Create a Tkinter window with a label and an entry box for the text to encode
window = tk.Tk()
label = tk.Label(window, text="Enter the URL you want for your QRcode:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to create the QR code
button = tk.Button(window, text="Create QR Code", command=create_qr)
button.pack()

# Start the Tkinter event loop
window.mainloop()
