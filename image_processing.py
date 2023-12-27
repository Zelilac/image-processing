import cv2
import numpy as np

def rotate_image(image, angle):
    # Implementasi fungsi rotasi seperti sebelumnya
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def translate_image(image, tx, ty):
    # Implementasi fungsi translasi seperti sebelumnya
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

def scale_image(image, scale_factor):
    # Implementasi fungsi skala seperti sebelumnya
    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    scale_matrix = np.float32([[scale_factor, 0, 0], [0, scale_factor, 0]])
    scaled_image = cv2.warpAffine(image, scale_matrix, (width, height))
    return scaled_image
