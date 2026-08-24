from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Conventional intrusion detection systems are limited in their
capacity to identify previously unknown attacks and adjust
to changing network conditions since they mostly rely on
predetermined signatures and expertly created rules. On the
other hand, discriminative patterns are directly learned from
data by machine learning-based intrusion detection systems,
making it possible to identify intricate and non-linear assault
behaviors. Because traffic patterns in EVSE situations
are dynamic and diverse, this data-driven capability is very
beneficial. Additionally, machine learning techniques show
reduced false alarm rates and increased detection accuracy,
which makes them better suited for safeguarding contemporary
EV charging infrastructures.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)