import cv2
import numpy as np

# Load the test image
image_path = 'State Ballot Tests/Dalmau and Pablo Jose (cross - bad vote).png'
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)

# Define coordinates for checkboxes
checkboxes = {
    "Partido Nuevo Progresista": (497, 334, 114, 84),
    "Partido Popular Democrático": (1058, 334, 114, 84),
    "Movimiento Victoria Ciudadana": (1619, 334, 114, 84),
    "Partido Independentista Puertorriqueño": (2180, 334, 114, 84),
    "Proyecto Dignidad": (2742, 335, 113, 83),
    "Jennifer González": (355, 636, 77, 52),
    "William Villafañe": (355, 817, 77, 52),
    "Jesús Manuel Ortiz": (917, 636, 77, 52),
    "Pablo José Hernández Rivera": (917, 817, 77, 52),
    "Javier Córdova Iturregui": (1479, 636, 76, 52),
    "Ana Irma Rivera Lassén": (1479, 817, 76, 52),
    "Juan Dalmau": (2041, 636, 76, 51),
    "Roberto Karlo Velázquez Correa": (2040, 818, 75, 50),
    "Javier Jiménez Pérez": (2603, 636, 76, 51),
    "Viviana Ramírez Morales": (2603, 817, 76, 51),
    "Write-in Gobernador": (3165, 636, 76, 51),
    "Write-in Comisionado Residente": (3165, 817, 76, 51)
}

# Draw rectangles around checkboxes
for candidate, (x, y, w, h) in checkboxes.items():
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with rectangles
cv2.imshow('Checkboxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()