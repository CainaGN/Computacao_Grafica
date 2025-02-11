import cv2
import numpy as np

def normalize_intensity(image):
    image = image.astype(np.float32)
    
    normalized = np.zeros_like(image, dtype=np.float32)
    

    for i in range(3):  
        min_val = np.min(image[:,:,i])
        max_val = np.max(image[:,:,i])
        normalized[:,:,i] = 255 * (image[:,:,i] - min_val) / (max_val - min_val + 1e-5)
    

    normalized = np.clip(normalized, 0, 255).astype(np.uint8)
    return normalized


image = cv2.imread('input.jpg')

normalized_image = normalize_intensity(image)

cv2.imwrite('output_5.jpg', normalized_image)

print("Imagem processada e salva como output_normalized.jpg")

