import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalize_histogram(image):
    # Calcular o histograma
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    
    # Calcular a CDF
    cdf = hist.cumsum()
    
    # Normalizar a CDF
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # Aplicar a equalização de histograma
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # Mapear os valores de intensidade da imagem original para a CDF
    image_equalized = cdf[image]
    
    return image_equalized


image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)

# Equalizar o histograma
image_equalized = equalize_histogram(image)


cv2.imwrite('output_equalized.jpg', image_equalized)

# Exibir a imagem original e a equalizada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Imagem Equalizada')
plt.imshow(image_equalized, cmap='gray')

plt.show()

