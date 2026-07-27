from backend.services.text_splitter import split_text

text = "Hello " * 1000

chunks = split_text(text)

print(f"Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk[:100])