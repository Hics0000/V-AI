from backend.memory.history import history


class Memory:

    def save_user(self, message: str):
        history.add("user", message)

    def save_assistant(self, message: str):
        history.add("assistant", message)

    def get_history(self):
        return history.get()

    def clear(self):
        history.clear()


memory = Memory()