from ollama import chat


class LLM:

    def __init__(self):
        self.model = "llama3.2"

    def ask(self, messages):

        response = chat(
            model=self.model,
            messages=messages
        )

        return response["message"]["content"]


llm = LLM()