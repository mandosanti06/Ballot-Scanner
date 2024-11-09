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
    "Movimiento Victoria Ciudadana": (1619, 334, 114, 84)
}

# Draw rectangles around checkboxes
for candidate, (x, y, w, h) in checkboxes.items():
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with rectangles
cv2.imshow('Checkboxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()