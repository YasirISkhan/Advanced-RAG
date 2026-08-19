from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'CohereLabs/tiny-aya-global',
    task = 'text-generation'
)
model = ChatHuggingFace(llm=llm)

result = model.invoke('What is the capital of Pakistan?')

print(result.content)