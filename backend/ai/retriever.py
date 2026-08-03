from backend.services.vector_store import vector_store



class Retriever:

    def retrieve(self, question: str):

        result = vector_store.search(question)

        documents = result["documents"][0]

        return "\n\n".join(documents)


retriever = Retriever()