import pdfplumber
from pdf2image import convert_from_path
import os
from src.ocr_utils import extract_text_from_image


def extract_text_from_pdf(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""

    return text


def extract_text_from_scanned_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    full_text = ""

    for i, img in enumerate(images):
        img_path = f"temp_page_{i}.png"
        img.save(img_path, "PNG")

        text = extract_text_from_image(img_path)
        full_text += text + "\n"

        os.remove(img_path)

    return full_text
