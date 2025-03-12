import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "Asia/Kolkata",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Pacific/Auckland",
    "Africa/Nairobi",
    "America/Los_Angeles",
    "Europe/Paris",
    "Asia/Tokyo",
]



st.title("Time Zone App")

selected_timezone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC"])

st.subheader("Selected Time Zones")

for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")
    


st.subheader("Convert Time Zone")

current_time = st.time_input("Select Time", datetime.now().time())
from_tz = st.selectbox("From Time Zone", TIME_ZONES,index=0)
to_tz = st.selectbox("To Time Zone", TIME_ZONES,index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    
    st.success(f"Converted Time in {to_tz}: {converted_time}")