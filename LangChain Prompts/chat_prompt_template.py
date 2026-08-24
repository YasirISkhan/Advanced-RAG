from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a {domain} expert'),
    ('human', 'Tell me about {topic}')
])

result = chat_template.invoke({'domain': 'cybersecurity', 'topic': 'Adversarial attacks'})

print(result)