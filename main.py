import streamlit as st
st.write("Hello, World!")

st.title("Title")
st.header("Header")
st.subheader("Sub-header")


st.title("Simple Web Form with Streamlit")
st.header("User Information Users")
name = st.text_input("Enter your name: ")
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an option: ", options)
