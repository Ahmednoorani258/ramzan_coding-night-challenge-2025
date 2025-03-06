from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelance writing",
    "Social media management",
    "Web development",
    "Graphic design",
    "Photography",
    "Virtual assistant",
]

money_quotes = [
    "Money is a terrible master but an excellent servant.",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver.",
    "Money is a guarantee that we may have what we want in the future. Though we need nothing at the moment, it ensures the possibility of satisfying a new desire when it arises.",
]
@app.get("/side-hustles")
def get_side_hustles(apikey: str):
    if apikey != "1234567890":
        return {"error": "Invalid Api Key"}
    return {"side_hustles": random.choice(side_hustles)}


@app.get("/money-quotes")
def get_money_quotes():
    return {"money_quotes": random.choice(money_quotes)}
