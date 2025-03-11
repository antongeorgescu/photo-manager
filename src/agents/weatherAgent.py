# filepath: weather-agent/src/agents/weatherAgent.py
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI, AzureChatOpenAI
from weatherService import fetch_weather_data
import os

# Load environment variables from .env file
load_dotenv()

# Define a simple tool function that retrieves weather information
def get_weather_info(location):
    """Fetches weather information for a given location."""
    # Placeholder for actual weather fetching logic
    return fetch_weather_data(location)

# List of tools available to the agent
tools = [
    Tool(
        name="WeatherInfo",
        func=get_weather_info,
        description="Useful for retrieving weather information for a specified location",
    ),
]

# Pull the prompt template from the hub
prompt = hub.pull("hwchase17/react-chat")

# Initialize a ChatOpenAI model
# llm = ChatOpenAI(
#     model="gpt-4o-mini", temperature=0
# )

llm = AzureChatOpenAI(
    openai_api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
    max_retries = 3
)

# Create the ReAct agent using the create_react_agent function
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
)

# Create an agent executor from the agent and tools
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    output_keys = ["city","country","temperature","unit","timestamp"]
)

# Run the agent with a test query
response = agent_executor.invoke({
    "input": "What's the weather like in London?",
    "chat_history":[]
})

if len(response['output'])>0:
    print("Answer:", response['output'])
    exit()

# Print the response from the agent
print("response:", f'Answer: Weather in {response["city"]}, {response["country"]} is {response["temperature"]}°C at {response["timestamp"]}')