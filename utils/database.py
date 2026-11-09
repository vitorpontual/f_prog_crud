import json 
import os

def load_json(nome_do_arquivo):
    filepath = f"database/{nome_do_arquivo}"
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_json(nome_do_arquivo, data):
    os.makedirs('database', exist_ok=True)
    filepath = f"database/{nome_do_arquivo}"
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
