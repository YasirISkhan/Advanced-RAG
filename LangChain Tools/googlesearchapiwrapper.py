from langchain_community.utilities import GoogleSerperAPIWrapper

search_tool = GoogleSerperAPIWrapper()

result = search_tool.invoke('Muneeba mazari release news')

print(result)