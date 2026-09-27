from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from dotenv import load_dotenv
import requests

load_dotenv()

llm = HuggingFaceEndpoint(
    model='meta-llama/Llama-3.1-8B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

@tool
def multiply(a:int , b:int) -> int:
    """Multiply a with b and return the result"""
    return a*b

model_with_tool = model.bind_tools([multiply])

result = model_with_tool.invoke('multiply 3 with 10')

print(multiply.invoke(result.tool_calls[0]))
