import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

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
    
    formatted_history = []
    for msg in history:
        role = "user" if msg["role"] == "user" else "assistant"
        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}]})
    
    try:
        # Generate response from the model
        response = model.generate_content(formatted_history)
        
        # Debugging: Check the response object
        if not response or not hasattr(response, 'text'):
            raise ValueError("The response from the model is invalid or missing the 'text' attribute.")
        
        # Append the assistant's response to the history
        history.append({"role": "assistant", "content": response.text})
        cl.user_session.set("history", history)
        
        # Send the response back to the user
        await cl.Message(content=response.text).send()
    
    except Exception as e:
        # Log the error for debugging
        print(f"Error generating response: {e}")
        await cl.Message(content="Sorry, I couldn't process your request. Please try again later.").send()