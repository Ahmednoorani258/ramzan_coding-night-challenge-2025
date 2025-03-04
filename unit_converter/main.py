import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion={
        "meter_kilometer":0.001,
        "kilometer_meter":1000,
        "gram_kilogram":0.001,
        "kilogram_gram":1000,

    }
    
    key = f"{from_unit}_{to_unit}"
    
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return "Not a valid conversion"
    
st.title("Unit Converter")

value = st.number_input("Enter the value to convert")
from_unit = st.selectbox("From", ["meter", "kilometer", "gram", "kilogram"])
to_unit = st.selectbox("To", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.write(result)