# Detecção de Rostos em Tempo Real

Este script em Python utiliza a biblioteca OpenCV para realizar a detecção de rostos em tempo real através de uma webcam.

## Como Funciona

1. **Importação da Biblioteca:** O código começa importando a biblioteca `cv2`, que é a interface Python para o OpenCV.

2. **Carregamento do Classificador:** Um classificador pré-treinado baseado no algoritmo Haar Cascade é carregado utilizando o arquivo `haarcascade_frontalface_default.xml`. Este classificador é usado para detectar rostos nas imagens capturadas.

3. **Captura de Vídeo:** O script acessa a webcam do computador usando `cv2.VideoCapture(0)`, onde `0` indica o dispositivo de captura de vídeo padrão (normalmente a webcam principal).

4. **Loop de Detecção:** O código entra em um loop infinito onde:
    - Uma imagem (frame) é capturada da webcam.
    - A imagem é convertida para tons de cinza, pois a detecção de rostos é mais eficaz em imagens monocromáticas.
    - A função `detectMultiScale` é utilizada para identificar rostos na imagem. Essa função retorna as coordenadas dos rostos detectados.
    - Para cada rosto detectado, um retângulo azul é desenhado ao redor da face na imagem original.

5. **Exibição do Vídeo:** O vídeo com as detecções é exibido em uma janela chamada "Video". 

6. **Encerramento:** O loop continua até que a tecla `q` seja pressionada, momento em que a captura de vídeo é liberada e todas as janelas do OpenCV são fechadas.

## Requisitos

- Python 3.x
- OpenCV (`cv2`)

## Como Executar

1. Instale o OpenCV, caso ainda não tenha instalado:
    ```bash
    pip install opencv-python
    ```
2. Certifique-se de que o arquivo `haarcascade_frontalface_default.xml` esteja disponível no mesmo diretório do script ou especifique o caminho correto para ele.
3. Execute o script:
    ```bash
    python detectar_rosto.py
    ```

A janela de vídeo será exibida e, ao detectar um rosto, um retângulo azul será desenhado ao redor dele. Pressione `q` para encerrar a execução.
