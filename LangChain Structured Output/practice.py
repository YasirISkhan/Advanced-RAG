from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = "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"
model = ChatGroq(model_name="llama-3.1-8b-instant")

class Student(BaseModel):
    name: str = 'Yasir'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=4.0, default=4.0, description='A decimal value representing the cgpa of the candidate')

new_student = {'email': 'abc@gmail.com', 'cgpa': 3}

student =  Student(**new_student)

print(student)

