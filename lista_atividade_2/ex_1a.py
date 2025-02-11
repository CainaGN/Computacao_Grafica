import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalize_histogram(image):
    # Dividir a imagem em seus três canais: R, G e B
    channels = cv2.split(image)
    
    # Equalizar o histograma de cada canal separadamente
    eq_channels = []
    for channel in channels:
        hist, bins = np.histogram(channel.flatten(), 256, [0, 256])
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max() / cdf.max()
        cdf_m = np.ma.masked_equal(cdf, 0)
        cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
        cdf = np.ma.filled(cdf_m, 0).astype('uint8')
        eq_channel = cdf[channel]
        eq_channels.append(eq_channel)
    
    # Combinar os canais equalizados de volta em uma imagem RGB
    image_equalized = cv2.merge(eq_channels)
    
    return image_equalized


image = cv2.imread('input.jpg')

image_equalized = equalize_histogram(image)

cv2.imwrite('output_1.jpg', image_equalized)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(1, 2, 2)
plt.title('Imagem Equalizada')
plt.imshow(cv2.cvtColor(image_equalized, cv2.COLOR_BGR2RGB))

plt.show()

