import json
from datetime import date

FILE = "data.json"

def load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {
            "phrase_date": "",
            "phrase_text": "",
            "users": []
        }

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_data():
    return load()

def update_phrase(text):
    data = load()
    data["phrase_date"] = str(date.today())
    data["phrase_text"] = text
    save(data)

def add_user(user_id):
    data = load()
    if user_id not in data["users"]:
        data["users"].append(user_id)
        save(data)