import cv2
import numpy as np
from sklearn.cluster import KMeans

def quantize_image(image_path, k=16):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Imagem não pôde ser carregada do caminho: {image_path}")
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    

    pixels = image_rgb.reshape((-1, 3))

    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)
    

    quantized_pixels = kmeans.cluster_centers_.astype('uint8')[kmeans.labels_]
    

    quantized_image = quantized_pixels.reshape(image_rgb.shape)
    

    quantized_image_bgr = cv2.cvtColor(quantized_image, cv2.COLOR_RGB2BGR)
    

    output_path = 'output_quantized.jpg'
    cv2.imwrite(output_path, quantized_image_bgr)
    
    print(f"Imagem quantizada salva em: {output_path}")


quantize_image('input.jpg', k=16)

