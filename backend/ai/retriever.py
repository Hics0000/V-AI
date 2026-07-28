from backend.services.vector_store import vector_store


class Retriever:

    def retrieve(self, question: str):

        print("\n========== RETRIEVER ==========")
        print("Question:", question)

        result = vector_store.search(
            question,
            top_k=5
        )

        print("\nRaw Result:")
        print(result)

        print("\nDocuments:")
        print(result["documents"])

        print("\nMetadata:")
        print(result["metadatas"])

        print("================================\n")

        documents = result["documents"][0]

        return "\n\n".join(documents)


retriever = Retriever()