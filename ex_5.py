import cv2
import numpy as np

def normalize_intensity(image):
    # Converte a imagem para float32 para evitar problemas de overflow durante a normalização
    image = image.astype(np.float32)
    
    # Obtém o valor mínimo e máximo de intensidade na imagem
    min_val = np.min(image)
    max_val = np.max(image)
    
    # Aplica a transformação linear para normalizar os valores no intervalo [0, 255]
    normalized = 255 * (image - min_val) / (max_val - min_val + 1e-5)
    
    # Converte a imagem normalizada de volta para uint8
    normalized = np.clip(normalized, 0, 255).astype(np.uint8)
    return normalized

image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

normalized_image = normalize_intensity(image)
cv2.imwrite('output_normalized.jpg', normalized_image)

print("Imagem processada e salva como output_normalized.jpg")

