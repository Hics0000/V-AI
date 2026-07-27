from backend.services.vector_store import vector_store

results = vector_store.search("your test question")

print(results)