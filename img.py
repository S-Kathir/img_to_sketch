import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def convert_to_sketch(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inverted_image = cv2.bitwise_not(gray_image)

    # Apply Gaussian blur to the inverted image
    #blurred_image = cv2.GaussianBlur(inverted_image, (111, 111), 0)

    # Invert the blurred image to get the sketch effect
    sketch_image = cv2.bitwise_not(inverted_image)

    return sketch_image

def browse_image():
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.jpeg; *.png")])
    if filename:
        img = Image.open(filename)
        img.thumbnail((400, 400))  # Resize image for display
        img = ImageTk.PhotoImage(img)
        canvas.image = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        global image_path
        image_path = filename

def convert_image():
    if image_path:
        sketch = convert_to_sketch(image_path)
        cv2.imshow('Sketch', sketch)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Create the main window
window = tk.Tk()
window.title("Image to Sketch Converter")

# Create the canvas to display the image
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the Browse button
browse_button = tk.Button(window, text="Browse", command=browse_image)
browse_button.pack()

# Create the Convert button
convert_button = tk.Button(window, text="Convert", command=convert_image)
convert_button.pack()

image_path = None

# Start the Tkinter event loop
window.mainloop()
