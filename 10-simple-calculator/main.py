import streamlit as st
def main():
    st.title("Simple Calculator")
    st.write("Enter two numbers and choose an operation:")
    
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter the first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter the second number", value=0.0)
        
    operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])
    
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero")
            return
        result = num1 / num2
    
    st.write(f"Result: {result}")

if __name__ == "__main__":
    main()