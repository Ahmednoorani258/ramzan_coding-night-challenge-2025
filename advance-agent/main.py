from dotenv import load_dotenv
import os
import chainlit as cl
from typing import Dict, Optional
from agents import Agent, Runner,AsyncOpenAI,OpenAIChatCompletionsModel
from agents.tool import function_tool

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 

provider = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider
)

@function_tool("get_weather")
def get_weather(location:str,unit:str = "C") -> str:
    """
    Fetch the weather for a given location, return the weather in the specified unit.
    """
    
    return f"The weather in {location} is 25{unit} and sunny."

agent = Agent(
    name = "Greeting Agent",
    instructions = "You are a customer service agent. You are tasked with greeting customers and providing them with the information they need. if some one says 'hello' you should respond with 'assalamualaikum from Ahmed Noorani,and if some one say bye you should respond with 'allahafiz form ahmed noorani!' when some one asks other than greeting or weather tell them that u are only hire for gretings related talks",
    model=model,
    tools=[get_weather]
    
    
)

@cl.oauth_callback
def oauth_callback(provider_id:str,token:str,raw_user_data:Dict[str,str],default_user:cl.User) -> Optional[cl.User]:
    
    print(f"provider_id: {provider_id}")
    print(f"user_Data: {raw_user_data}")
    
    return default_user


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content = "Hello! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})
    
    result = await cl.make_async(Runner.run_sync)(agent, input=history)
    response = result.final_output
    await cl.Message(content = response).send()
    
    history.append({"role": "agent", "content": response})
    cl.user_session.set("history", history)