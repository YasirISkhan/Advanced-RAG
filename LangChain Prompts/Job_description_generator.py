from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

template = PromptTemplate(
    template = """
    Act as a professional job description generator. The job title is {job_title} in a {company_industry}. Experience level is {experience_level}. And the key skills include {skills}. Create a structured job description containing responsibilities, requirements, and preferred skills.
    """,
    input_variables=['job_title', 'company_industry', 'experience_level', 'skills'],
    template_validate = True
)

prompt = template.invoke({'job_title':'Data Engineer', 'company_industry': 'Healthcare', 'experience_level': 'mid-level', 'skills': 'Python, SQL, AWS'})

result = model.invoke(prompt)

print(result.content)