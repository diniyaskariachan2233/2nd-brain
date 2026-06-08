import json
import os

FILE_PATH = "data/memory_store.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f)

def store_memory(text, embedding):
    data = load_data()
    data.append({
        "text": text,
        "embedding": embedding
    })
    save_data(data)

def get_all_memories():
    return load_data()
