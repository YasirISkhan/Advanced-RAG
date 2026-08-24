from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200, 
    chunk_overlap=0
)

text = """
# Introduction to Artificial Intelligence

Artificial Intelligence (AI) is a branch of computer science that focuses on building systems that can perform tasks that normally require human intelligence.

## Machine Learning

Machine Learning (ML) is a subset of AI that enables computers to learn patterns from data without being explicitly programmed.

### Types of Machine Learning

There are three common types of machine learning:

- **Supervised Learning**: The model learns from labeled data.
- **Unsupervised Learning**: The model discovers patterns in unlabeled data.
- **Reinforcement Learning**: The model learns by interacting with an environment and receiving rewards or penalties.

## Deep Learning

Deep Learning is a specialized area of machine learning that uses artificial neural networks with multiple layers.

### Applications of Deep Learning

Deep learning is widely used in:

1. Image classification
2. Natural language processing
3. Speech recognition
4. Autonomous vehicles
5. Medical image analysis

## Large Language Models

Large Language Models (LLMs) are deep learning models trained on large collections of text.

LLMs can perform tasks such as:

- Text generation
- Question answering
- Summarization
- Translation
- Code generation

## Conclusion

Artificial Intelligence is rapidly transforming many industries. Machine Learning, Deep Learning, and Large Language Models are important technologies that are contributing to this transformation.
"""

result = splitter.split_text(text)

print(result[0])