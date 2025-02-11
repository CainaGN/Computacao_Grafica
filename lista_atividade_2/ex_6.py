import cv2
import numpy as np

def correct_errors_with_std(image_path, output_path, window_size=50, k=1.5):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Imagem não pôde ser carregada do caminho: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corrected_image = np.copy(gray)

    rows, cols = gray.shape

    offset = window_size // 2
    for i in range(offset, rows - offset):
        for j in range(offset, cols - offset):
            window = gray[i - offset:i + offset + 1, j - offset:j + offset + 1]
            
            mean, std_dev = np.mean(window), np.std(window)
            
            if abs(gray[i, j] - mean) > k * std_dev:
                corrected_image[i, j] = mean

    corrected_bgr = cv2.cvtColor(corrected_image, cv2.COLOR_GRAY2BGR)
    
    cv2.imwrite(output_path, corrected_bgr)
    
    print(f"Imagem corrigida e salva como {output_path}")

correct_errors_with_std('input_2.jpeg', 'output_corrected.jpg')

