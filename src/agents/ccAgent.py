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

from typing import List
import json

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
def create_nonregistered_student(firstname:str,lastname:str,homeAddress:str) -> str:
    """Create non-registered student and return student id."""
    log_tool_usage("create_nonregistered_student", json.dumps({"firstName":firstname,"lastName":lastname,"homeAddress":homeAddress}))
    studentinfo = {"studentid": 1, "firstName": firstname, "lastName": lastname, "homeAddress": homeAddress}
    return json.dumps(studentinfo)

@tool
def add_communication_info(studentid :int, phoneNumber:str, email:str, preference:str) -> str:
    """Assign communication info to a non-registered student."""
    log_tool_usage("add_communication_info", json.dumps({"studentid":studentid,"phoneNumber":phoneNumber,"email":email,"preference":preference}))
    communication = {"studentid": studentid, "phoneNumber": phoneNumber, "email": email, "preference": preference}
    return json.dumps(communication)

@tool
def create_loan(studentid:int, loaninfo: List[str], collegecode:str, programofstudy:str) -> str:
    """Assign to a non-registered student a loan, a college and a program of study."""
    log_tool_usage("create_loan", {studentid,json.dumps(loaninfo),collegecode,programofstudy})
    return json.dumps(loaninfo)

@tool
def find_student_by_lastname(lastname :str) -> str:
    """Retrieve student information based on likeness to last name."""
    log_tool_usage("find_student_by_lastname", lastname)
    return lastname

  
tools = [create_nonregistered_student, add_communication_info,create_loan,find_student_by_lastname]

llm_with_tools = llm.bind_tools(tools)

MEMORY_KEY = "chat_history"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            # "You are very powerful assistant, but bad at managing students, communication, loans, education institutions and programs of study. Can you help me with that?",
            "You are very powerful assistant, but bad at managing students and communication. Can you help me with that?",
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