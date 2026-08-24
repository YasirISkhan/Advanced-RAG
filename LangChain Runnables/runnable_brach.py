from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Summarize the following text \n {text}',
    input_variables=['text']
)

llm = HuggingFaceEndpoint(
    repo_id = 'CohereLabs/tiny-aya-global',
    task = 'text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic': 'Iran VS America'})

print(result)