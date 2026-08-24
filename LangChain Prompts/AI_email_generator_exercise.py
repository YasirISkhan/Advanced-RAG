from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

template = PromptTemplate(
    template = """
    Draft a concise, compelling cold email to a {prospect_role} in the {company_industry} industry.
    Highlight how our product helps them: {value_proposition}.
    Keep the tone professional yet approachable. Don't write extra details. 
    """,
    input_variables = ['prospect_role', 'company_industry', 'value_proposition'],
    validate_template=True
)

prompt = template.invoke({'prospect_role': 'HR Team', 'company_industry': 'Information Technology', 'value_proposition': 'helping companies automate data workflows using AI, reducing cybersecurity risks through intelligent threat detection, or building scalable data pipelines for better business analytics'})

result = model.invoke(prompt)

print(result.content)