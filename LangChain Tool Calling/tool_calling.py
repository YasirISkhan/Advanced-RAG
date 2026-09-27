from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

@tool
def multiply(a:int, b:int)-> int:
    "Given two numbers a and b this tool returns their product"
    return a*b

llm_with_tools = model.bind_tools([multiply])

print(llm_with_tools.invoke('Can you multiply 3 with 10'))