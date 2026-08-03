from backend.ai.prompt import SYSTEM_PROMPT
from backend.ai.llm import llm
from backend.ai.retriever import retriever
from backend.memory.memory import memory


class RAG:

    def ask(self, question: str):

        context = retriever.retrieve(question)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(memory.get_history())

        messages.append(
            {
                "role": "system",
                "content": f"Context:\n{context}"
            }
        )

        messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        answer = llm.ask(messages)

        memory.save_user(question)
        memory.save_assistant(answer)

        return answer


rag = RAG()