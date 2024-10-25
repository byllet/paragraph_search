from model import get_embedding
import uuid


PARAGRAPHS = []


def add_to_paragraphs(text):
    embedding = get_embedding(f"passage: {text}")
    PARAGRAPHS.append({
        "id": str(uuid.uuid4()),
        "passage": text,
        "embedding": embedding
    })


def indexing_data(data):
    add_to_paragraphs(data)
