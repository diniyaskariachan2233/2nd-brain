import numpy as np
from app.database.vector_store import get_all_memories

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_memory(query_embedding, top_k=3):
    memories = get_all_memories()

    if not memories:
        return []

    scored = []

    for mem in memories:
        score = cosine_similarity(query_embedding, mem["embedding"])
        scored.append((score, mem["text"]))

    scored.sort(reverse=True)

    return [text for _, text in scored[:top_k]]
