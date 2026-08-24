from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

class Person(TypedDict):
    name: str
    age: int

new_person = Person({'name': 'Yasir', 'age': 27})

print(new_person)
