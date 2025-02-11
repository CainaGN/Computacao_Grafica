import cv2
import numpy as np

def suavizar(imagem):
    novaImagem = np.copy(imagem)
    
    # Converte a imagem para float32 para evitar overflow
    imagem = imagem.astype(np.float32)
    
    for linha in range(2, len(imagem) - 2):
        for coluna in range(2, len(imagem[linha]) - 2):
            soma = 0
            for l in range(linha - 2, linha + 3):  
                for c in range(coluna - 2, coluna + 3):  
                    soma += imagem[l, c]
            media = soma / 25.0
            novaImagem[linha, coluna] = media
    return novaImagem

if __name__ == "__main__":
    imagem = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)  
    imagemSuavizada = suavizar(imagem)
    cv2.imwrite('output_mean_filter.jpg', imagemSuavizada)

