import cv2
import pytesseract

# Get the file path from the user using input
image_path = input("Enter the image file path: ")

# Load the image
image = cv2.imread(image_path)

# Configure Tesseract OCR for text recognition
pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract.exe'

# Perform text recognition
text = pytesseract.image_to_string(image)

# Print the recognized text
print(text)
