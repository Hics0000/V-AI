import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="data/chroma")
        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_document(self, chunks):
        embeddings = self.model.encode(chunks).tolist()

        self.collection.add(
            ids=[str(i) for i in range(len(chunks))],
            documents=chunks,
            embeddings=embeddings
        )

    def search(self, question, top_k=3):
        embedding = self.model.encode([question])[0].tolist()

        result = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )

        return result["documents"][0]


vector_store = VectorStore()