from backend.services.vector_store import vector_store

results = vector_store.collection.get()

print("=" * 50)
print(f"Total Chunks: {len(results['ids'])}")
print("=" * 50)

for i, metadata in enumerate(results["metadatas"]):
    print(f"Chunk {i+1}")
    print(f"Filename : {metadata['filename']}")
    print(f"Chunk No : {metadata['chunk']}")
    print("-" * 30)