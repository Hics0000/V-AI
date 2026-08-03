from backend.memory.memory import memory

memory.save_user("Hello")
memory.save_assistant("Hi!")

print(memory.get_history())