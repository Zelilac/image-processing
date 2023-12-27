import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from image_processing import rotate_image, translate_image, scale_image

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        # Variabel untuk menyimpan path gambar
        self.image_path = ""

        # Variabel untuk menyimpan parameter
        self.rotation_var = tk.DoubleVar()
        self.translation_x_var = tk.DoubleVar()
        self.translation_y_var = tk.DoubleVar()
        self.scale_var = tk.DoubleVar()

        # Membuat antarmuka pengguna
        self.create_widgets()

    def create_widgets(self):
        # Button untuk memilih gambar
        choose_image_button = tk.Button(self.root, text="Choose Image", command=self.load_image)
        choose_image_button.pack(pady=10)

        # Slider untuk menentukan sudut rotasi
        rotation_slider = tk.Scale(self.root, label="Rotation Angle", from_=0, to=360, orient=tk.HORIZONTAL, variable=self.rotation_var)
        rotation_slider.pack(pady=10)

        # Slider untuk menentukan translasi x
        translation_x_slider = tk.Scale(self.root, label="Translation X", from_=-200, to=200, orient=tk.HORIZONTAL, variable=self.translation_x_var)
        translation_x_slider.pack(pady=10)

        # Slider untuk menentukan translasi y
        translation_y_slider = tk.Scale(self.root, label="Translation Y", from_=-200, to=200, orient=tk.HORIZONTAL, variable=self.translation_y_var)
        translation_y_slider.pack(pady=10)

        # Slider untuk menentukan faktor skala
        scale_slider = tk.Scale(self.root, label="Scale Factor", from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL, variable=self.scale_var)
        scale_slider.pack(pady=10)

        # Button untuk memproses gambar
        process_button = tk.Button(self.root, text="Process Image", command=self.process_image)
        process_button.pack(pady=10)

    def load_image(self):
        # Memilih gambar menggunakan file dialog
        self.image_path = filedialog.askopenfilename()

    def process_image(self):
        # Memeriksa apakah gambar sudah dipilih
        if not self.image_path:
            print("Pilih gambar terlebih dahulu.")
            return

        # Membaca citra
        original_image = cv2.imread(self.image_path)

        # Mendapatkan nilai parameter dari slider
        rotation_angle = self.rotation_var.get()
        translation_x = self.translation_x_var.get()
        translation_y = self.translation_y_var.get()
        scale_factor = self.scale_var.get()

        # Memanggil fungsi rotasi
        rotated_image = self.rotate_image(original_image, rotation_angle)

        # Memanggil fungsi translasi
        translated_image = self.translate_image(rotated_image, translation_x, translation_y)

        # Memanggil fungsi skala
        scaled_image = self.scale_image(translated_image, scale_factor)

        # Menampilkan citra asli, citra yang telah dirotasi, di-translasi, dan di-skala
        cv2.imshow('Original Image', original_image)
        cv2.imshow('Rotated Image', rotated_image)
        cv2.imshow('Translated Image', translated_image)
        cv2.imshow('Scaled Image', scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
