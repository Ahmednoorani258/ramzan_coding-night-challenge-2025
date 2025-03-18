import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

while True:
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")

    userinput= input("Enter your question: ")
    if userinput == "exit":
        print("Goodbye!")
        break

    response = model.generate_content(userinput)

    print(response.text)