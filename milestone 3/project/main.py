from ner import extract_entities
from gpt_parser import parse_with_gpt
from rules import map_rules
from utils import safe_json_parse

def process_note(note):
    print("\n--- INPUT ---")
    print(note)

    # Step 1: Extract entities
    entities = extract_entities(note)
    print("\nEntities:", entities)

    # Step 2: GPT parsing
    gpt_output = parse_with_gpt(note)
    parsed = safe_json_parse(gpt_output)

    print("\nGPT Parsed:", parsed)

    # Step 3: Rule mapping
    rules = map_rules(note)

    print("\nMapped Rules:", rules)

    return {
        "entities": entities,
        "parsed": parsed,
        "rules": rules
    }


if __name__ == "__main__":
    sample_note = "Patient has diabetes. Avoid sugar. High fiber diet recommended."

    result = process_note(sample_note)
    print("\nFINAL OUTPUT:\n", result)
