import cv2
import numpy as np

def suavizar_mediana(imagem):
    novaImagem = np.copy(imagem)
    
    rows, cols, _ = imagem.shape
    
    for i in range(3): 
        for linha in range(2, rows - 2):
            for coluna in range(2, cols - 2):

                janela = []
                for l in range(linha - 2, linha + 3):  
                    for c in range(coluna - 2, coluna + 3):  
                        janela.append(imagem[l, c, i])

                media_mediana = np.median(janela)
                novaImagem[linha, coluna, i] = media_mediana
    return novaImagem

if __name__ == "__main__":
    imagem = cv2.imread('input.jpg') 
    imagemSuavizada = suavizar_mediana(imagem)
    cv2.imwrite('output_7.jpg', imagemSuavizada)

