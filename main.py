# Reconocimiento de imagenes   /// OpenCV

import cv2
from superposicion import superposicion 
from reconocimiento_simple import reconocimiento_simple

imagen_monedas_simple = cv2.imread('monedas.jpg')
imagen_monedas_superpuestas = cv2.imread('monedas_2.jpg')

contornos, jerarquia = reconocimiento_simple(imagen_monedas_simple)
contornos2, jerarquia2 = superposicion(imagen_monedas_superpuestas)

print("monedas encontradas imagen simple: {}" .format(len(contornos)))
print("monedas encontradas imagen compleja: {}" .format(len(contornos2)))

# Dibujar contorno
cv2.drawContours(imagen_monedas_simple, contornos, -1, (251, 60, 50), 3)
cv2.drawContours(imagen_monedas_superpuestas, contornos2, -1, (251, 60, 50), 3)
# Mostrar imagen
#cv2.imshow('imagen', imagen_contorno)
cv2.imshow('imagen monedas1', imagen_monedas_simple)
cv2.imshow('imagen monedas2', imagen_monedas_superpuestas)
cv2.waitKey(0)

cv2.destroyAllWindows()

