RULES_DB = {
    "low sodium": {"nutrient": "sodium", "limit": "1500mg/day"},
    "avoid sugar": {"nutrient": "sugar", "action": "avoid"},
    "high protein": {"nutrient": "protein", "level": "high"},
    "high fiber": {"nutrient": "fiber", "level": "high"}
}

def map_rules(parsed_text):
    mapped = []

    for key, value in RULES_DB.items():
        if key in parsed_text.lower():
            mapped.append(value)

    return mapped
