from sklearn.metrics.pairwise import cosine_similarity


from model import get_embedding
from paragraphs import PARAGRAPHS


def query(q, k):
    query_embedding = get_embedding(f"query: {q}") 
    similarities = []

    for doc in PARAGRAPHS:
        score = cosine_similarity(query_embedding, doc['embedding'])[0][0]
        if score > 0.5:
            similarities.append({'text': doc['passage'],
                                 'score': float(score)})

    similarities.sort(key=lambda x: x['score'], reverse=True)
    return similarities[:k]


def find_top_k(text, top_k):
    return query(text, top_k)
