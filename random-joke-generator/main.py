import streamlit as st
import requests

def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
            
        else:
            return ("No jokes available")
    except:
        return st.warning("something went wrong")

def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random joke:")
    if st.button("Generate Joke"):
        joke = get_random_joke()
        st.success(joke)

if __name__ == "__main__":
    main()

