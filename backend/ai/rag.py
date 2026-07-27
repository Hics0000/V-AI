from backend.ai.llm import llm
from backend.ai.retriever import retriever


class RAG:

    def ask(self, question: str):

        context = retriever.retrieve(question)

        prompt = f"""
You are V.

Answer ONLY from the context below.

If the answer is not present, reply:
'I don't have information about that.'

Context:
{context}

Question:
{question}
"""

        return llm.ask(prompt)


rag = RAG()