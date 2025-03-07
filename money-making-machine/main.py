import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(2)
    st.success(f"Congratulations! You have generated ${generate_money()}")
    

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money-quotes")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["money_quotes"]
        else:
            return ("No money quotes available")
        
    except:
        return st.warning("something went wrong")
    

def fetch_side_hustles():
    try:
        url = "http://127.0.0.1:8000/side-hustles"
        params = {"apikey": "1234567890"}  

        response = requests.get(url, params=params) 
        
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustles", "No side hustles found.")
        else:
            return f"Error: {response.status_code} - {response.text}"

    except requests.RequestException as e:
        return f"Request failed: {str(e)}"

st.subheader("Money Quotes")
if st.button("Get Money Quote"):
    idea = fetch_money_quotes()
    st.success(idea)
    

st.subheader("Side Hustles")
if st.button("Get Side Hustle Idea"):
    hustle = fetch_side_hustles()
    st.success(hustle)