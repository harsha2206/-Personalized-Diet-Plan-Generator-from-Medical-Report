import re

def extract_medical_data(text):
    data = {}

    patterns = {
        "hemoglobin": r"Hemoglobin[:\s]+([\d.]+)",
        "glucose": r"Glucose[:\s]+([\d.]+)",
        "cholesterol": r"Cholesterol[:\s]+([\d.]+)",
        "platelets": r"Platelets[:\s]+([\d.]+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data[key] = float(match.group(1))

    return data
