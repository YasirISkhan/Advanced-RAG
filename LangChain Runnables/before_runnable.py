import random

class Dummy:
    def __init__(self):
        print('LLM created')

    def predict(self, prompt):
        response_list = [
            'Islamabad is the capital of Pakistan',
            'PSL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        
        return {'response': random.choice(response_list)}
    
llm = Dummy()
llm.predict('What is the capital of Pakistan?')


class Dummer:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)
    

template = Dummer(
    template='Write a {length} poem about {topic}',
    input_variables=['length','topic']
)

prompt = template.format({'length': 'short','topic': 'Pakistan'})

llm = Dummy()

llm.predict(prompt)


class MeraChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']
    
template = Dummer(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

chain = MeraChain(llm, template)

print(chain.run({'length': 'short', 'topic': 'Pakistan'}))
