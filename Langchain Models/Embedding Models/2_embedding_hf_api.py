from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

print("Connecting to Hugging Face Cloud Inference API for Embeddings...")

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2", # LangChain uses 'model' here instead of 'model_name'
    task="feature-extraction"                       
)

text = "What is the Capital of Pakistan?"


query_result = embeddings.embed_query(text)
print("\n--- Success! ---")
print(f"Vector generated completely in the cloud!")
print(f"Vector length (dimensions): {len(query_result)}")
print(f"First 5 dimensions: {query_result[:5]}")
