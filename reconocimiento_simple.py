import cv2

def reconocimiento_simple(imagen):
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    valorGauss = 5
    valorKernel = 5

    imagen_gris_suavizado = cv2.GaussianBlur(imagen_gris, (valorGauss, valorKernel), 0)

    imagen_gris_sin_ruido = cv2.Canny(imagen_gris_suavizado, 50 ,150, cv2.THRESH_BINARY_INV )

    # Aplicar operaciones morfológicas para cerrar contornos y agrupar áreas cercanas
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    imagen_morfologia = cv2.morphologyEx(imagen_gris_sin_ruido, cv2.MORPH_CLOSE, kernel)

    # Encontrar los contornos después de aplicar morfología
    contornos, jerarquia = cv2.findContours(imagen_morfologia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contornos, jerarquia