import streamlit as st

# Set the title of the web page
st.title("Simple Web Form with Streamlit")

# Set a header
st.header("User Information Users")
# Text input for name
name = st.text_input("Enter your name: ")
# Dropdown menu for selecting an option
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.selectbox("Choose an Option:", options)
# Slider for selecting a value 

# Submit button
if st.button("Sumbit"):
    st.write(f"Name; {name}")
    st.write(f"Selected Option: {selected_option}")
# Additional information

# Footer

