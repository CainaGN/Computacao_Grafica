import cv2
import numpy as np

def increase_brightness(image, value):
    result = np.zeros_like(image, dtype=np.uint8)

    rows, cols, _ = image.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(3):  # Itera sobre os canais (B, G, R)
                new_value = int(image[i, j, k]) + value
                result[i, j, k] = min(255, max(0, new_value))

    return result

image = cv2.imread('input.jpg')

image_bright = increase_brightness(image, 20)

cv2.imwrite('output_2.jpg', image_bright)

print("Imagem processada e salva como output_2.jpg")

