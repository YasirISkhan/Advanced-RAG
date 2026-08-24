from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'CohereLabs/tiny-aya-global',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {topic}',
    input_variables=['topic']
)

joke_gen = RunnableSequence(prompt1, model, parser)

runnable_passthrough = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen, runnable_passthrough)

result = final_chain.invoke({'topic': 'AI'})

print(result)