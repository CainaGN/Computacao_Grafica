import cv2
import numpy as np

def is_gray_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Imagem não pôde ser carregada. Verifique o caminho da imagem.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bgr_from_gray = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    if np.array_equal(image, bgr_from_gray):
        print("A imagem é em escala de cinza.")
        return True
    else:
        print("A imagem é colorida.")
        return False


image_path = 'input.jpg'
is_gray_image(image_path)

