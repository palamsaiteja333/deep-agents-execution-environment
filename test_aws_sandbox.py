
from deepagents import create_deep_agent
from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter
from langchain_agentcore_codeinterpreter import AgentCoreSandbox

from models import model

interpreter = CodeInterpreter(region="us-east-2")
interpreter.start()

backend = AgentCoreSandbox(interpreter=interpreter)

agent = create_deep_agent(
    model=model,
    backend=backend,
    system_prompt=(
        "You are a coding assistant. "
        "Write Python scripts to files before executing them. "
        "Show the execution output."
    ),
)

try:
    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": (
                "Write a Python script that prints the first "
                "15 Fibonacci numbers, save it to fib.py, "
                "and execute it."
            )
        }]
    })

    print(result["messages"][-1].content)

finally:
    interpreter.stop()
