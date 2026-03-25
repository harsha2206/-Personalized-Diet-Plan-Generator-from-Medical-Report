import spacy

nlp = spacy.load("en_core_web_sm")

MEDICAL_TERMS = {
    "diabetes": "condition",
    "hypertension": "condition",
    "sodium": "nutrient",
    "sugar": "nutrient",
    "protein": "nutrient",
    "fiber": "nutrient"
}

def extract_entities(text):
    doc = nlp(text.lower())
    entities = []

    for token in doc:
        if token.text in MEDICAL_TERMS:
            entities.append({
                "text": token.text,
                "type": MEDICAL_TERMS[token.text]
            })

    return entities
