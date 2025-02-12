# Processamento de Imagens - Computação Gráfica

Este repositório contém implementações de algoritmos de processamento de imagens desenvolvidos para a disciplina de Computação Gráfica do curso de Engenharia de Computação no IFMS - Campus Três Lagoas.

O repositório está organizado em dois diretórios:

- **Lista 1 - Processamento em Níveis de Cinza**: Contém algoritmos aplicados a imagens em tons de cinza, incluindo equalização de histograma, ajuste de brilho e contraste, transformações logarítmicas, normalização, e filtros de suavização.

- **Lista 2 - Processamento de Imagens Coloridas (RGB)**: Expansão das técnicas da Lista 1 para imagens coloridas, além de novos algoritmos como contagem de cores, detecção de temperatura de cor, verificação de imagens coloridas ou em tons de cinza, quantização de cores e recuperação de desenhos rabiscados.

As implementações utilizam as bibliotecas OpenCV (`cv2`), NumPy (`numpy`), Matplotlib (`matplotlib.pyplot`) e Scikit-Learn (`scikit-learn.cluster`).

## Dependências
Instale as bibliotecas necessárias antes de executar os códigos:
```bash
pip install opencv-python numpy matplotlib scikit-learn
```

## Como Executar
Cada funcionalidade está em um arquivo separado dentro dos diretórios correspondentes. Para rodar um script:
```bash
python caminho/para/o/arquivo.py
```
Certifique-se de que a imagem de entrada (`input.jpg`) está no mesmo diretório do script.

