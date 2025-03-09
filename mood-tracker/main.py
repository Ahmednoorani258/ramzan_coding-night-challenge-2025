import streamlit as st
import pandas as pd
import datetime 
import csv
import os

MOOD_File = "mood_log.csv"


def load_mood_data():
    if not os.path.exists(MOOD_File):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_File)

def save_mood_data(date,mood):
    with open(MOOD_File, mode= 'a') as file:
        
        writer = csv.writer(file)
        writer.writerow([date, mood])


st.title("Mood Tracker")

today = datetime.date.today()
st.subheader("How are you feeling today?")

mood = st.selectbox("Select Mood", ["Happy", "Neutral", "Sad", "Angry", "Stressed", "Excited", "Tired", "Anxious", "Confused", "Bored", "Calm", "Grateful", "Hopeful", "Lonely", "Nostalgic", "Optimistic", "Peaceful", "Proud", "Relaxed", "Silly", "Surprised", "Thankful", "Worried", "Other"])

if st.button("Save mood"):
    save_mood_data(today, mood)
    st.success("Mood saved successfully!")
    
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Log")
    data["Date"] = pd.to_datetime(data["Date"])
    mood_count = data.groupby('Mood').count()['Date']
    
    st.bar_chart(mood_count)
    # st.dataframe(data)
