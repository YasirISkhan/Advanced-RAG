from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document
from langchain.schema import Document

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create LangChain documents for PSL players
doc1 = Document(
    page_content="Babar Azam is one of the most successful and consistent batsmen in PSL history. Known for his aggressive batting style and fitness, he has led the Peshawar Zalmi in multiple seasons.",
    metadata={"team": "Peshawar Zalmi"}
)
doc2 = Document(
    page_content="Shaheen Afridi is the most successful captain in PSL history, leading Lahore Qalandars to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
    metadata={"team": "Lahore Qalandars"}
)
doc3 = Document(
    page_content="Mohammad Rizwan, famously known as Captain Cool, has led Multan Sultans to multiple PSL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
    metadata={"team": "Multan Sultans"}
)
doc4 = Document(
    page_content="Haris Rauf is considered one of the best fast bowlers in T20 cricket. Playing for Islamabad United, he is known for his yorkers and death-over expertise.",
    metadata={"team": "Islamabad United"}
)
doc5 = Document(
    page_content="Shadab Khan is a dynamic all-rounder who contributes with both bat and ball. Representing Quetta Gladiators, his quick fielding and match-winning performances make him a key player.",
    metadata={"team": "Quetta Gladiators"}
)

# list of all documents
docs = [doc1, doc2, doc3, doc4, doc5]

vector_store = Chroma(
    embedding_function = embedding_model,
    persistent_directory = 'my_chroma_db',
    collection_name='sample'
)

