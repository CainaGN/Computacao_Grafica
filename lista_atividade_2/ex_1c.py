import cv2
import numpy as np

def adjust_contrast(image, alpha):
    result = np.zeros_like(image, dtype=np.uint8)

    rows, cols, _ = image.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(3):  
                new_value = alpha * (int(image[i, j, k]) - 128) + 128
                result[i, j, k] = min(255, max(0, int(new_value)))

    return result

image = cv2.imread('input.jpg')

image_contrast = adjust_contrast(image, 1.5)

cv2.imwrite('output_3.jpg', image_contrast)

print("Imagem processada e salva como output_contrast.jpg")

