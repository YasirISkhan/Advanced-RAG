from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

document = [
    "Babar Azam is a Pakistani cricketer known for his tok-tok batting.",
    "Salman Ali Agha is believed to be a nothing batsman who is believed to be parchi.",
    "Hassan Nawaz is a middle order batsman who is known for his aggressive batting.",
    "Shaheen is believed to be a speedstar who often takes a wicket in his first over of the match."
]

query = "Tell me about Babar Azam"

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

print(list(enumerate(scores)))