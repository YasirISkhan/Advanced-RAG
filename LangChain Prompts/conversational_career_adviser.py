from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

chat_history = [
    
]

chat_template = ChatPromptTemplate([
    ('system', 'You are a conversational career adviser chatbot'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

prompt = chat_template.invoke({'chat_history': chat_history,'query':'How can I become an AI Engineer?'})

result = model.invoke(prompt)
print(result.content)

