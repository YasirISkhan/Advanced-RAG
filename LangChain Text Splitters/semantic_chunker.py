from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings


# Load an open-source embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create semantic chunker
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="interquartile"
)

# Sample text
text = """
Artificial Intelligence is transforming healthcare.
Machine learning models can analyze medical images and help doctors
identify diseases.

Solar energy is becoming an important source of renewable energy.
Modern solar panels can generate electricity from sunlight and are
being used in homes and large power plants.

Natural Language Processing allows computers to understand and process
human language. Large language models are an important application of
NLP and can generate human-like text.
"""

# Split text into semantic chunks
chunks = text_splitter.create_documents([text])

# Display chunks
for i, chunk in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(chunk.page_content)