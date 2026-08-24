from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=200,
    chunk_overlap=0
)

code = """
class Student:
    
    def introduce(self):
        print("Hello! My name is Yasir.")
    
    def study(self):
        print("I am learning Python and Machine Learning.")


# Create an object of the class
student = Student()

# Call both methods
student.introduce()
student.study()
"""

result = splitter.split_text(code)

print(result[0])