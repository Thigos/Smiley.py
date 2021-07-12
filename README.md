# Reconhecer e Seguir
Esse é um programa que reconhece e segue rostos, a partir de uma câmera, utilizando visão computacional.

### Requisitos:

| Nome         | Versão <br> recomendada|
|----------------|------|
| Python | 3.6+ |
| OpenCV         | 4.5+ |
| OpenCV-Contrib | 4.5+ |

### Configurar Câmera

Na linha 6 do ```Smiley.py``` está localizada a variavel para configuração da câmera ```cap = cv2.VideoCapture(0)```, por padrão a maioria das webcams vem com o ID 0. Caso a sua câmera seja uma exceção, pesquise no google pelo modelo e o ID dela.

### Funcionamento

Usando um algoritmo de aprendizado (Haar Cascade), o programa detecta e segue o rosto de uma pessoa, utilizando 2 desenhos de "olhos".

