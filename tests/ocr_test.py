import cv2
import pytesseract
import easyocr

# ==============================
# CONFIGURACIÓN DE TESSERACT
# ==============================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ==============================
# IMAGEN DE PRUEBA
# ==============================
imagen = "tests/1.jpg"

# ==============================
# OCR con Tesseract
# ==============================
print("=== OCR con Tesseract ===")
img = cv2.imread(imagen)
texto_tesseract = pytesseract.image_to_string(img, lang="spa")  
print(texto_tesseract)

# ==============================
# OCR con EasyOCR
# ==============================
print("\n=== OCR con EasyOCR ===")
reader = easyocr.Reader(['es'])  
resultado_easyocr = reader.readtext(imagen, detail=0)
print(" ".join(resultado_easyocr))

# ==============================
# Comparación simple
# ==============================
print("\n=== Comparación rápida ===")
print(f"Tesseract: {len(texto_tesseract.split())} palabras detectadas")
print(f"EasyOCR:   {len(resultado_easyocr)} palabras detectadas")
