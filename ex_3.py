import cv2
import numpy as np

def adjust_contrast(image, alpha):
    # Cria uma cópia da imagem para modificar
    result = np.zeros_like(image, dtype=np.uint8)

    # Obtém as dimensões da imagem
    rows, cols = image.shape

    # Percorre cada pixel
    for i in range(rows):
        for j in range(cols):
            # Aplica a transformação linear de contraste garantindo que não haja overflow
            new_value = alpha * (int(image[i, j]) - 128) + 128
            # Garante que o valor esteja no intervalo [0, 255]
            result[i, j] = min(255, max(0, int(new_value)))

    return result


image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

image_contrast = adjust_contrast(image, 1.5)

cv2.imwrite('output_contrast.jpg', image_contrast)

print("Imagem processada e salva como output_contrast.jpg")

