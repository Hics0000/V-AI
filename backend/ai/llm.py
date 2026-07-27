from ollama import chat


class LLM:

    def __init__(self):
        self.model = "llama3.2"

    def ask(self, question: str) -> str:

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]


llm = LLM()