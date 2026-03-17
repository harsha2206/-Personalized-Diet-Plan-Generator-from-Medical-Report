import pytesseract
import cv2
from PIL import Image

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise removal
    gray = cv2.medianBlur(gray, 3)

    # Thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return thresh


def extract_text_from_image(image_path):
    processed_img = preprocess_image(image_path)

    text = pytesseract.image_to_string(processed_img)
    return text
