# Processamento de Imagens em Python

Este repositório contém implementações em Python para  técnicas de processamento de imagens em escala de cinza. As aplicações utilizam as bibliotecas OpenCV (`cv2`), NumPy (`numpy`) e Matplotlib (`matplotlib.pyplot`). Todas as imagens de entrada devem ser nomeadas como `input.jpg`.

## Funcionalidades Implementadas

### 1. Equalização de Histograma
- Carrega uma imagem em níveis de cinza e aplica equalização de histograma.
- Salva a imagem resultante como `output_equalized.jpg`.

### 2. Transformação de Intensidade para Aumento de Brilho
- Utiliza uma imagem subexposta (com pouca iluminação) e aplica uma transformação de intensidade para aumentar o brilho.
- Salva a imagem resultante como `output_brightness.jpg`.
- Inclui uma análise comparativa com a imagem original, destacando as mudanças e o que permaneceu inalterado.

### 3. Ajuste de Contraste com Função Personalizada
- Implementa um método próprio para ajuste de contraste, sem utilizar equalização de histograma.
- Salva a imagem processada como `output_contrast.jpg`.

### 4. Transformação Logarítmica
- Aplica uma transformação logarítmica para ajustar a intensidade da imagem.
- Salva a imagem processada como `output_log.jpg`.
- Compara a imagem original e a processada para analisar as mudanças visuais.

### 5. Normalização de Intensidade
- Cria uma função para normalizar os níveis de intensidade de uma imagem para um intervalo fechado de 0 a 255.
- Testa a função com diferentes imagens.
- Salva as imagens normalizadas como `output_normalized.jpg`.

### 6. Aplicação de Filtro da Média (Suavização)
- Implementa um algoritmo para aplicar um filtro da média a uma imagem.
- Salva a imagem suavizada como `output_mean_filter.jpg`.

### 7. Aplicação de Filtro da Mediana
- Implementa um algoritmo para aplicar um filtro da mediana a uma imagem.
- Salva a imagem processada como `output_median_filter.jpg`.

## Dependências
Instalação de bibliotecas encessárias:
```bash
pip install opencv-python numpy matplotlib
```


