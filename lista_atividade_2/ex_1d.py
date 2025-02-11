import cv2
import numpy as np

def log_transform(image, intensity=0.5):
    image = image.astype(np.float32)
    
    result = np.zeros_like(image, dtype=np.float32)

    for i in range(3):  
        c = (255 / np.log(1 + np.max(image[:,:,i]))) * intensity
        result[:,:,i] = c * np.log(1 + image[:,:,i] + 1e-5)


    result = np.clip(result, 0, 255).astype(np.uint8)
    return result


image = cv2.imread('input.jpg')

image_log = log_transform(image, intensity=0.7)  

cv2.imwrite('output_4.jpg', image_log)

print("Imagem processada e salva como output_log.jpg")

