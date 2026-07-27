from backend.services.vector_store import vector_store


class Retriever:

    def retrieve(self, question: str):

        documents = vector_store.search(
            question,
            top_k=3
        )

        return "\n\n".join(documents)


retriever = Retriever()