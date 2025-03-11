import os
import asyncio
from typing import Any
from langchain_openai import AzureChatOpenAI
from langchain.agents import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain.agents import AgentExecutor
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

from weatherService import fetch_weather_data

llm = AzureChatOpenAI(
    openai_api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
    max_retries = 3
)

tool_usage_log = []

def log_tool_usage(tool_name: str, input_data: Any):
    """Logs the tool used and its input."""
    tool_usage_log.append({"tool": tool_name, "input": input_data})

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    log_tool_usage("get_word_length", word)
    return len(word)

@tool
def calculator(expression :str) -> str:
    """Evaluates mathematical expression"""
    log_tool_usage("calculator", expression)
    try:
        maths_result = eval(expression)
        return str(maths_result)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def get_weather_info(location: str) -> str:
    """Returns the weather information for a specified location."""
    log_tool_usage("get_weather_info", location)
    return fetch_weather_data(location)
    
tools = [get_word_length, calculator,get_weather_info]
llm_with_tools = llm.bind_tools(tools)

MEMORY_KEY = "chat_history"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are very powerful assistant, but bad at calculating lengths of words, mathematical expressions or fetching weather information. Can you help me with that?",
        ),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_tool_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | prompt
    | llm_with_tools
    | OpenAIToolsAgentOutputParser()
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

async def main():
    chat_history = []
    while True:
        print("Enter question or type exit to quit")
        input1 = input("User: ")

        if input1.lower() == "exit":
            print("Exiting the chat.")
            break

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, lambda: agent_executor.invoke({"input":input1 , "chat_history": chat_history}))

        chat_history.extend(
        [
            HumanMessage(content=input1),
            AIMessage(content=result["output"]),
        ]
    )
        print("\nTools Used:")
        for usage in tool_usage_log:
            print(f"Tool: {usage['tool']}, Input: {usage['input']}")
            
        print("\n\n Message:\n", result["output"])

if __name__ == "__main__":
    asyncio.run(main())