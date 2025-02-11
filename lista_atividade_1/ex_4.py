import cv2
import numpy as np

def log_transform(image, intensity=0.5):
    # Converte a imagem para float para evitar overflow
    image = image.astype(np.float32)
    
    # Define uma constante de escala ajustável
    c = (255 / np.log(1 + np.max(image))) * intensity

    # Aplica a transformação logarítmica com uma constante pequena para evitar log(0)
    result = c * np.log(1 + image + 1e-5)

    # Converte a imagem de volta para uint8
    result = np.clip(result, 0, 255).astype(np.uint8)
    return result

# Carregar a imagem em escala de cinza
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Ajustar o contraste da imagem usando transformação logarítmica
image_log = log_transform(image, intensity=0.7)  # Teste valores como 0.3, 0.5, 0.7 para ajustar

# Salvar a imagem resultante como "output_log.jpg"
cv2.imwrite('output_log.jpg', image_log)

print("Imagem processada e salva como output_log.jpg")

