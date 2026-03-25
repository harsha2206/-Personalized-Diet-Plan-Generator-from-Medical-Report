import json

def safe_json_parse(text):
    try:
        return json.loads(text)
    except:
        return {"error": "Invalid JSON", "raw": text}
