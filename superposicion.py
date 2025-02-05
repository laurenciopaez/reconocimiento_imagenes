import cv2
import numpy as np

def superposicion(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Suavizado (imagen borrosa)
    valorGauss = 15
    valorKernel = 15
    """ El valor de Gaus aplica una funcion Gaussiana (campana) para asignar pesos a los pixeles vecinos de cada pixel. Los pixeles cercanos al centro tienen mas peso, y los lejanos menos. A mas grande el Kernel mayor desenfoque. """
    imagen_gris_suavizado = cv2.GaussianBlur(imagen_gris, (valorGauss, valorKernel), 0)

# Eliminacion de ruidos
    """ Algoritmo de deteccion de bordes de Canny. Resalta los contornos de la imagen, eliminando variaciones peque;as que suelen ser consideradas como ruido."""
    imagen_gris_sin_ruido = cv2.Canny(imagen_gris_suavizado, 20 ,190, cv2.THRESH_BINARY_INV )

    kernel_superpuestas = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    # Operacion morfologica
    """ Se aplica una operacion morfologica a una imagen binaria. Puede ser:
cv2.MORPH_ERODE: erosión, reduce el tamaño de los objetos blancos.
cv2.MORPH_DILATE: dilatación, expande los objetos blancos.
cv2.MORPH_OPEN: apertura (erosión seguida de dilatación), ideal para eliminar ruido.
cv2.MORPH_CLOSE: cierre (dilatación seguida de erosión), ideal para cerrar huecos pequeños.
cv2.MORPH_GRADIENT: gradiente morfológico, destaca los contornos.
cv2.MORPH_TOPHAT: diferencia entre la imagen original y su apertura.
cv2.MORPH_BLACKHAT: diferencia entre la imagen cerrada y la original.
"""
    imagen_moneda_morfologia = cv2.morphologyEx(imagen_gris_sin_ruido, cv2.MORPH_TOPHAT, kernel_superpuestas)


    # Encontrar contorno para monedas superpuestas
    """ Calcula la transformada de distancia de una imagen binaria. Asigna a cada pixel el valor de la distancia minima hasta el pixel negro mas cercano (fondo)"""
    dist_transform = cv2.distanceTransform(imagen_moneda_morfologia, cv2.DIST_L2, 5) 
    _, sure_fg = cv2.threshold(dist_transform, 0.5* dist_transform.max(), 255, 0)

    # Marcar objetos encontrados superpuestos
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(imagen_moneda_morfologia, sure_fg)
    # Encontrar contornos
    contornos, jerarquia = cv2.findContours(sure_fg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contornos, jerarquia



