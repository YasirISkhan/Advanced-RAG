from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

chat_template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert'),
    ('human', 'Tell me difference between {topic}')
])

prompt = chat_template.invoke({'domain': 'AI', 'topic': 'langchain and langgraph'})

result = model.invoke(prompt)
print(result)