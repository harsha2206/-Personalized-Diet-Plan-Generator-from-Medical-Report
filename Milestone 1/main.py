import os
from src.extract_text import extract_text_from_pdf, extract_text_from_scanned_pdf
from src.parser import extract_medical_data


def process_file(file_path):
    print(f"Processing: {file_path}")

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)

        # fallback to OCR if empty
        if not text.strip():
            text = extract_text_from_scanned_pdf(file_path)

    elif file_path.endswith((".png", ".jpg", ".jpeg")):
        from src.ocr_utils import extract_text_from_image
        text = extract_text_from_image(file_path)

    else:
        with open(file_path, "r") as f:
            text = f.read()

    structured_data = extract_medical_data(text)

    return structured_data


if __name__ == "__main__":
    folder = "data/sample_reports"

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        result = process_file(file_path)
        print("Extracted Data:", result)
