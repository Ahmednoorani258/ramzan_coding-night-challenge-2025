import os 
from dotenv import load_dotenv
from agents import Agent, Runner,AsyncOpenAI,OpenAIChatCompletionsModel

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

agent = Agent(
    name = "Greeting Agent",
    instructions = "You are a customer service agent. You are tasked with greeting customers and providing them with the information they need. if some one says 'hello' you should respond with 'assalamualaikum from Ahmed Noorani,and if some one say bye you should respond with 'allahafiz form ahmed noorani!'",
    model=model
    
)

result = Runner.run_sync(agent,"hi")
print(result.final_output)