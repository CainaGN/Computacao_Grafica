import cv2
import numpy as np

def suavizar(imagem):
    novaImagem = np.zeros_like(imagem, dtype=np.float32)
    

    imagem = imagem.astype(np.float32)
    

    for i in range(3): 
        for linha in range(2, len(imagem) - 2):
            for coluna in range(2, len(imagem[linha]) - 2):
                soma = 0
                for l in range(linha - 2, linha + 3):  
                    for c in range(coluna - 2, coluna + 3):  
                        soma += imagem[l, c, i]
                media = soma / 25.0
                novaImagem[linha, coluna, i] = media
    

    novaImagem = np.clip(novaImagem, 0, 255).astype(np.uint8)
    return novaImagem

if __name__ == "__main__":
    imagem = cv2.imread('input.jpg')  
    imagemSuavizada = suavizar(imagem)
    cv2.imwrite('output_6.jpg', imagemSuavizada)

