import uuid

import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="data/chroma")

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_document(self, filename: str, chunks: list[str]):

        embeddings = self.model.encode(chunks).tolist()

        ids = [str(uuid.uuid4()) for _ in chunks]

        metadatas = [
            {
                "filename": filename,
                "chunk": index
            }
            for index in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, question: str, top_k: int = 3):

        embedding = self.model.encode([question])[0].tolist()

        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return result


vector_store = VectorStore()