from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

chat_template = ChatPromptTemplate([
    ('system', 'You are a patient {subject} tutor. Explain complex concepts to beginners using simple real-world analogies.'),
    ('human', 'Can you explain {topic} to me?')
])

prompt = chat_template.invoke({'subject': 'Computer Science', 'topic': 'Recusion'})

for msg in prompt.messages:
    print(f'Role: {msg.type.upper()}')
    print(f'Content: {msg.content}')

    