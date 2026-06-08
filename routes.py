from fastapi import APIRouter
from app.models import UserInput
from app.services.embedding import get_embedding
from app.services.retrieval import retrieve_memory
from app.services.ai_response import generate_response
from app.database.vector_store import store_memory

router = APIRouter()

@router.post("/chat")
def chat(input: UserInput):
    user_text = input.text

    # Step 1: Convert to embedding
    embedding = get_embedding(user_text)

    # Step 2: Store memory
    store_memory(user_text, embedding)

    # Step 3: Retrieve similar memories
    memories = retrieve_memory(embedding)

    # Step 4: Generate AI response
    response = generate_response(user_text, memories)

    return {
        "response": response,
        "related_memories": memories
    }
