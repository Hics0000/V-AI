from backend.ai.prompt import SYSTEM_PROMPT
from backend.ai.llm import llm
from backend.ai.retriever import retriever


class RAG:

    def ask(self, question: str, history=None):

        context = retriever.retrieve(question)

        conversation_history = ""

        if history:
            for message in history:
                conversation_history += (
                    f"{message.role}: {message.content}\n"
                )

        prompt = f"""
{SYSTEM_PROMPT}

CONVERSATION HISTORY:
{conversation_history}

DOCUMENT INFORMATION:
{context}

CURRENT QUESTION:
{question}

RULES:
- First check the conversation history.
- Then check the document information.
- If either source contains the answer, answer using that information.
- Do not say that information is unavailable if it exists in the conversation history.
- Do not invent information.
- Give a short, natural answer.
"""

        return llm.ask(prompt)


rag = RAG()