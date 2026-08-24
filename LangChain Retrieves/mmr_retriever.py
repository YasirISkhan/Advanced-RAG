from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


docs = [
    Document(page_content='Langchain helps developers build LLM applications easily.'),
    Document(page_content='Chroma is a vector database optimized for LLM-based search.'),
    Document(page_content='Embeddings convert text into high-dimensional vectors'),
    Document(page_content='HuggingFace provides open source embedding models.')
]

embedding_model = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
)

vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = 'mmr',
    search_kwargs = {"k": 3, "lambda_mult":0.5}
)

query = 'What is langchain'

results = retriever.invoke(query)

print(results)