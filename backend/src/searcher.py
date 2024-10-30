from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer


class Searcher:
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.model = SentenceTransformer("intfloat/multilingual-e5-large")
        self.qdrant_client = QdrantClient("http://qdrant:6333")
        self.collection_name = collection_name

        if not self.qdrant_client.collection_exists(self.collection_name):
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.model.get_sentence_embedding_dimension(),
                    distance=models.Distance.COSINE,
                )
            )
            
        self.index_ = 0


    def search(self, text: str, top_k: int):
        vector = self.model.encode(text).tolist()

        search_result = self.qdrant_client.query_points(
            collection_name=self.collection_name,
            query=vector,
            query_filter=None,
            limit=top_k,
        ).points

        payloads = [hit.payload for hit in search_result]
        return payloads
    

    def index(self, content):
        points = []

        for paragraph in content:

            if 'content' not in paragraph:
                return -1
            
            points.append(models.PointStruct(
                        id=self.index_, vector=self.model.encode(paragraph['content']).tolist(), payload=paragraph
                    )
                )
            
            self.index_ += 1

        self.qdrant_client.upload_points(
            collection_name=self.collection_name,
            points=points
        )

        return 1
