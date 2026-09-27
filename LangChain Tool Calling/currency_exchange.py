from langchain_core.tools import tool
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from dotenv import load_dotenv
import json

load_dotenv()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""

    url = f'https://v6.exchangerate-api.com/v6/Your-api-key/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()

print(get_conversion_factor.invoke({'base_currency': 'USD', 'target_currency': 'PKR'}))


@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) ->float:
    """Given a currency conversion rate this fuction calculates the target curency value from a given base currency value"""

    return base_currency_value * conversion_rate

result = convert.invoke({'base_currency_value': 10, 'conversion_rate': 85.16})


llm = HuggingFaceEndpoint(
    model = 'meta-llama/Llama-3.1-8B-Instruct',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

llm_with_tool = model.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage('What is the conversion factor between USD and PKR, and based on that can you convert 10 usd to PKR')]

ai_message = llm_with_tool.invoke(messages)

messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        messages.append(tool_message1)

    if tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)


final = llm_with_tool.invoke(messages).content

print(final)