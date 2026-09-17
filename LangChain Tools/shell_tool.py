from langchain_community.tools import ShellTool

Shell_tool = ShellTool()

result = Shell_tool.invoke('whoami')

print(result)