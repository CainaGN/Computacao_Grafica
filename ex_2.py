import cv2
import numpy as np

def increase_brightness(image, value):
    # Cria uma cópia da imagem para modificar
    result = np.zeros_like(image, dtype=np.uint8)

    # Obtém as dimensões da imagem
    rows, cols = image.shape

    # Percorre cada pixel
    for i in range(rows):
        for j in range(cols):
            # Aumenta o valor do pixel, garantindo que ele esteja dentro do intervalo [0, 255]
            new_value = int(image[i, j]) + value
            result[i, j] = min(255, max(0, new_value))

    return result


image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Aumentar o brilho de cada pixel em 20, limitando a 255
image_bright = increase_brightness(image, 20)
cv2.imwrite('output_brightness.jpg', image_bright)

print("Imagem processada e salva como output_brightness.jpg")

