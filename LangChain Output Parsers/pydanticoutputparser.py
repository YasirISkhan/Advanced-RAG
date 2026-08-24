from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'CohereLabs/tiny-aya-global',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

class Book(BaseModel):
    name: str = Field(description='Name of the book')
    pages: int = Field(description='Number of pages in the book')
    author: str = Field(description='Author of the book')


parser = PydanticOutputParser(pydantic_object=Book)

template = PromptTemplate(
    template = 'Name, pages, and author of the fictional {title} book \n {format_instruction}',
    input_variables=['title'],
    partial_variables = {"format_instruction": parser.get_format_instructions()}
)

prompt = template.invoke({'title': 'Urdu'})

result = model.invoke(prompt)

final_result = parser.parse(result.text)

print(final_result)

