# Reconocimiento de Imágenes con OpenCV

Este proyecto utiliza OpenCV para realizar el reconocimiento de monedas en imágenes. Se desarrollaron dos métodos diferentes para manejar casos sencillos y complejos (con monedas superpuestas).

## Descripción

Se utilizan dos enfoques para el reconocimiento de monedas:

1. **Reconocimiento Simple**: Utiliza un procesamiento básico de imágenes (conversión a escala de grises, suavizado y detección de bordes) para detectar monedas en una imagen sencilla.
2. **Superposición de Monedas**: Utiliza un procesamiento morfológico avanzado y transformada de distancia para detectar monedas superpuestas en una imagen más compleja.

Ambos métodos devuelven los contornos de las monedas detectadas y muestran los resultados visualmente.

## Requisitos

- Python 3.x
- OpenCV (`cv2`)
- NumPy

## Instalación

Instalar las dependencias necesarias:

```bash
pip install opencv-python numpy
